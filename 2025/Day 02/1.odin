//
// thought process:
//
// try to see the pattern
//
// 1. only an even number of digits, the odd ones can be discarded
// 2. the first half has to be the same as the second half, and
//    viceversa
//
//     v                          v     v
// 10 11 12 13 14 15 .. 19 20 21 22 .. 33       etc.
//
// w/ four digits:
// 1010 .. 1111 .. 1212 .. 1313
// => equivalent to counting 10, 11, 12, .., 99, so 2 digit numbers
// 
// for example, in the range from 100_000 up to 999_999, the amount of
// invalid IDs is obtained by counting the amount of numbers with 3
// digits, so 100 to 999 => 899.
//
// if the range doesn't start cleanly, for example it's 323_467, use
// the first half as the starting point & "clamp" it with the second half
// (for example in this case 323_323 is not included, so we just start
// from 324).  we do something similar if the range doesn't end
// cleanly.
//
// if the end doesn't even have the same number of digits tho, we have
// to split it into more ranges probably, and then solve the problem in
// the same way.  => Actually, atleast in my input the difference in
// digits is at most 1, so one of the "sides" will fall in odd digits
// which we don't care about, so we don't need something too
// complicated.
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

parse_halfs :: proc(s: string) -> (first_half: int, second_half: int) {
    assert(len(s) % 2 == 0)
    half_digits := len(s) / 2
    first_half,  _ = strconv.parse_int(s[:half_digits])
    second_half, _ = strconv.parse_int(s[half_digits:])
    return
}

main :: proc() {
    raw_data, _ := os.read_entire_file_from_filename("input.txt")
    data := string(raw_data)
    // I wish I could trim the last newline in a less verbose and OS
    // independent way, this should work tho
    newline :: "\r\n" when ODIN_OS == .Windows else "\n"
    data = strings.trim_suffix(data, newline)

    invalid_ids := 0

    for range in strings.split_iterator(&data, ",") {
        s := strings.split(range, "-")

        // These refer to the inclusive ranges of halfs of invalid IDs
        start, end: int

        if len(s[0]) % 2 == 0 {
            first_half, second_half : int = parse_halfs(s[0])
            start = first_half
            if second_half > first_half do start += 1
        } else {
            // If the start of the range has and odd amount of digits, assume
            // the end will not be like that and place the start accordingly
            half_digits := len(s[0]) / 2
            start = pow10_i(half_digits)
        }

        if len(s[1]) % 2 == 0 {
            first_half, second_half : int = parse_halfs(s[1])
            end = first_half
            if second_half < first_half do end -= 1
        } else {
            // Idem
            half_digits := len(s[1]) / 2
            end = pow10_i(half_digits) - 1
        }

        // fmt.println(s, start, end)

        // Iterate through the halfs of invalid IDs, and sum the invalid IDs
        for half_invalid_id in start..=end {
            digits := math.count_digits_of_base(half_invalid_id, base=10)
            invalid_ids += half_invalid_id + pow10_i(digits) * half_invalid_id
            assert(invalid_ids >= 0) // detect overflow
        }
    }

    fmt.println(invalid_ids)
}
