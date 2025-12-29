package day_01

import "core:os"
import "core:fmt"
import "core:strings"
import "core:strconv"


main :: proc() {
    data_raw, ok := os.read_entire_file_from_filename("input.txt")
    assert(ok)
    data := string(data_raw)

    dial := 50
    pointing_at_zero_counter := 0

    for line in strings.split_lines_iterator(&data) {
        multiplier := 1 if line[0] == 'R' else -1
        value, ok := strconv.parse_int(line[1:])
        assert(ok)

        // "Invert" value of dial if going to the left
        normalized_dial := dial if multiplier == 1 else (100 - dial) % 100
        // Add how many times the dial pointed to 0 while rotating
        pointing_at_zero_counter += (normalized_dial + value) / 100

        dial += multiplier * value
        // we use remainder instead of modulo to always stay positive :D
        dial %%= 100
    }

    fmt.println(pointing_at_zero_counter)
}
