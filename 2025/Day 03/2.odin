// 
// this can be done similarly to part 1, but with 12 "passes" instead of only
// 2.  the time complexity is at most O(12*N) for each bank, so it's fine.
//
// the process would be like this:
// 1. find the (first instance of the) max power and its index.
// 2. if the index is not in the last 12 of the bank, then we can use it as our
// first digit of joltage.  then, we can just go back to step 1 but with the
// right subset of the bank (everything after the max power).
//
// otherwise use it as the n-th digit, were n is equal to 12 minus the distance
// until the end of the bank.  in fact, all the powers to the right of that one
// will have to be used as the digits to the right of it, so we can just repeat
// the step 1 but with: the left subset of the bank instead of the whole bank,
// and n-1 digits instead of 12.  then we can re-construct the whole 12-digit
// joltage.
//

package day_03

import "core:fmt"
import "core:os"
import "core:strings"
import "core:strconv"
import "core:math"

// power of 10 with integers, converting without a care in the world
pow10_i :: proc(x: int) -> int {
    return int(math.pow10(f64(x)))
}

find_joltage :: proc(bank: string, joltage_digits: int
    ) -> (joltage: int) {

    if joltage_digits == 0 do return

    assert(len(bank) >= joltage_digits)

    // find the (first instance of the) max power and its index.
    max_power := '0'
    max_power_i := 0
    for power, i in bank {
        if power > max_power {
            max_power = power
            max_power_i = i
        }
    }

    // were "digit" means an index in the joltage result.  if negative, it
    // means it can be used as the first digit and the next digits need to be
    // searched for.
    digit_to_use_as := joltage_digits - (len(bank) - max_power_i)
    if digit_to_use_as < 0 {
        // use max_power for joltage[0]
        digits_left := joltage_digits - 1
        joltage = pow10_i(digits_left) * int(max_power - '0')
        joltage += find_joltage(bank[max_power_i+1:], digits_left)
    } else {
        // use bank[max_power_i:] for joltage[digit_to_use_as:]
        digits_left := digit_to_use_as
        digits_on_the_right_side := len(bank) - max_power_i
        joltage = pow10_i(digits_on_the_right_side) * find_joltage(bank[:max_power_i], digits_left)
        right_side, _ := strconv.parse_int(bank[max_power_i:])
        joltage += right_side
    }

    return joltage
}

main :: proc() {
    raw_data, _ := os.read_entire_file_from_filename("input.txt")
    data := string(raw_data)
    newline := "\r\n" when ODIN_OS == .Windows else "\n"
    data = strings.trim_suffix(data, newline)

    total_output_joltage := 0

    for line in strings.split_lines_iterator(&data) {
        bank_joltage := find_joltage(line, 12)
        total_output_joltage += bank_joltage
        assert(total_output_joltage >= 0) // detect overflow
    }

    fmt.println(total_output_joltage)
}
