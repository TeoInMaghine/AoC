package day_01

import "core:os"
import "core:fmt"
import "core:strings"
import "core:strconv"


main :: proc() {
    // I don't need to deallocate because it'll just get freed when the program
    // terminates. Normally there would be a defer delete(data_raw).
    data_raw, ok := os.read_entire_file_from_filename("input.txt")
    assert(ok)
    data := string(data_raw)

    dial := 50
    pointing_at_zero_counter := 0

    for line in strings.split_lines_iterator(&data) {
        multiplier := 1 if line[0] == 'R' else -1
        value, ok := strconv.parse_int(line[1:])
        assert(ok)

        dial += multiplier * value
        // we use remainder instead of modulo to always stay positive :D
        dial %%= 100
        if dial == 0 do pointing_at_zero_counter += 1
    }

    fmt.println(pointing_at_zero_counter)
}
