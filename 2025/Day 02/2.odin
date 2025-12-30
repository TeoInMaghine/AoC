//
// this can be solved similarly to part 1, but iterating through the amount of
// digits that get repeated.  since we already solved part 1 in a really
// efficient way, we can afford doing that (and there aren't that many digits
// anyway).
//
// instead of thinking of halfs of the numbers, we can think of for example 1
// digit repeating, or 2 digits repeating, and so on (as long as it divides the
// total amount of digits cleanly).  for example:
//      number = 54764 => digits = 5
//
//  1 digit repeating : digits (5) % 1 == 0 and digits / 1 == 5 >= 2 => ok
//  2 digits repeating: digits % 2 == 1  => not ok, has to be 0
//  ...
//  5 digits repeating: digits % 5 == 0 and digits / 5 == 1 => not ok, has to be >= 2
//
//  ( actually, I just realized that digits / repeating_digits will always be
//  greater or equal to 2 if we iterate through amounts of digits from 1 to
//  digits/2, so the second check isn't necessary )
//
//  if ok, we can parse the numbers (in this case only each individual digit):
//  number => {5, 4, 7, 6, 4}
//
//    > the clamp checking would have to happen for each digit in this case, so
//    > start = 5, if 4 > start => start += 1, otherwise if 7 > start => start += 1,
//    > and so on (in this case 7 > 5, so start = 5 + 1 = 6).
//
// (maybe it'd be cheaper/easier to actually check if start/end invalid ID is
// inside the range and add/subtract one if it isn't?) => I ended up doing this
//
//

package day_02

import "core:fmt"
import "core:os"
import "core:strings"
import "core:strconv"
import "core:math"

// power of 10 with integers, converting without a care in the world
pow10_i :: proc(x: int) -> int {
    return int(math.pow10(f64(x)))
}

// creates an invalid id from the number to repeat, how many digits that number
// has, and how many times that number should be repeated
get_invalid_id :: proc(num_to_repeat, digits, count: int) -> int {
    invalid_id := 0
    multiplier := pow10_i(digits)
    for _ in 0..<count {
        invalid_id *= multiplier
        invalid_id += num_to_repeat
    }
    return invalid_id
}

get_limit :: proc(id: string, repeating_digits: int, lower_limit: bool
    ) -> (limit: int) {

    first_part, _ := strconv.parse_int(id[:repeating_digits])
    id_num,     _ := strconv.parse_int(id)
    possible_first_invalid_id := get_invalid_id(
        first_part, repeating_digits, len(id) / repeating_digits)
    
    limit = first_part
    if lower_limit {
        if possible_first_invalid_id < id_num do limit += 1
    } else {
        if possible_first_invalid_id > id_num do limit -= 1
    }
    return limit
}

main :: proc() {
    raw_data, _ := os.read_entire_file_from_filename("input.txt")
    data := string(raw_data)
    // I wish I could trim the last newline in a less verbose and OS
    // independent way, this should work tho
    newline :: "\r\n" when ODIN_OS == .Windows else "\n"
    data = strings.trim_suffix(data, newline)

    invalid_ids := 0

    // we allocate these dynamic things only once, and clear them instead of
    // deleting them

    // possible_digits will always have at most 2 elements
    possible_digits := make([dynamic]int, 0, 2)
    // we may find repeated invalid ids, we register them to not over-count them
    found_invalid_ids := make(map[int]bool)

    for range in strings.split_iterator(&data, ",") {
        s := strings.split(range, "-")
        first_id, last_id := s[0], s[1]


        for repeating_digits in 1..=max(len(first_id), len(last_id))/2 {

            // the repeating digits may fit cleanly on the first id, the last
            // id, or both; we add them to the possible digits accordingly. we
            // don't add both if they're the same, to avoid unnecessary work.
            if len(first_id) % repeating_digits == 0 {
                append(&possible_digits, len(first_id))
            }
            if len(last_id) % repeating_digits == 0 && len(first_id) != len(last_id) {
                append(&possible_digits, len(last_id))
            }
            for digits in possible_digits {

                // fmt.printfln("digits: %v - repeating digits: %v", digits, repeating_digits)

                start := get_limit(first_id, repeating_digits, true) if
                         len(first_id) == digits else
                         pow10_i(repeating_digits-1)

                end   := get_limit(last_id, repeating_digits, false) if
                         len(last_id) == digits else
                         pow10_i(repeating_digits) - 1

                // fmt.println(s, start, end)

                for repeating_part in start..=end {
                    found_invalid_id := get_invalid_id(
                        repeating_part, repeating_digits, digits / repeating_digits)
                    if found_invalid_id in found_invalid_ids do continue
                    found_invalid_ids[found_invalid_id] = true

                    // fmt.println(found_invalid_id)
                    invalid_ids += found_invalid_id
                    assert(invalid_ids >= 0) // detect overflow
                }
            }

            clear(&possible_digits)
        }

        // we don't need to register all invalid ids, only the ones within each
        // range, so we clear it
        clear(&found_invalid_ids)
    }

    fmt.println(invalid_ids)
}
