// 
// we need to find the digits that produce the biggest 2-digit number.
// I think one valid strategy would be:
// - find the biggest number.
// - if there are other numbers after it, find the biggest number after that
//   one and use it as the second digit.
// - if it's the last number, then find the second biggest number and use that
//   one as the first digit.
//

package day_03

import "core:fmt"
import "core:os"
import "core:strings"

main :: proc() {
    raw_data, _ := os.read_entire_file_from_filename("input.txt")
    data := string(raw_data)
    newline := "\r\n" when ODIN_OS == .Windows else "\n"
    data = strings.trim_suffix(data, newline)

    total_output_joltage := 0

    for line in strings.split_lines_iterator(&data) {
        biggest_power := 0
        biggest_power_i := 0
        second_biggest_power := 0

        for rune, i in line {
            power := int(rune - '0')

            // if the sequence of numbers is non-increasing, the second biggest
            // power will be equal to 0, but it doesn't matter because it's
            // only used when the biggest power is the last one, which cannot
            // happen in a non-increasing sequence :P
            if power > biggest_power {
                second_biggest_power = biggest_power
                biggest_power = power
                biggest_power_i = i
            }
        }

        bank_joltage: int
        if biggest_power_i == len(line) - 1 {
            bank_joltage = 10 * second_biggest_power + biggest_power
        } else {
            next_max_power := 0
            for rune in line[biggest_power_i+1:] {
                next_max_power = max(next_max_power, int(rune - '0'))
            }
            bank_joltage = 10 * biggest_power + next_max_power
        }

        total_output_joltage += bank_joltage
        assert(total_output_joltage >= 0) // detect overflow
    }

    fmt.println(total_output_joltage)
}
