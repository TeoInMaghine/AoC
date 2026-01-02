package day_06

import "../common"
import "core:fmt"
import "core:strings"
import "core:unicode/utf8"
import "core:slice"
import "core:math"

main :: proc() {
    using strings

    data := common.get_input_file_contents()

    rows := count(data, common.newline)
    cols := index(data, common.newline)

    // needed for parsing data
    line_length := cols + len(common.newline)

    // parse the vertical numbers, with separators between groups
    SEPARATOR :: -1
    numbers: [dynamic]int
    col_builder := builder_make(0, rows)
    for col_i in 0..<cols {
        for row_i in 0..<rows {
            rune := utf8.rune_at_pos(data, line_length*row_i + col_i)
            if rune != ' ' do write_rune(&col_builder, rune)
        }
        if builder_len(col_builder) != 0 {
            append(&numbers, common.parse_int(to_string(col_builder)))
        }
        else do append(&numbers, SEPARATOR)
        builder_reset(&col_builder)
    }

    // move data to the last line of the file
    row_i := 0
    for line in split_lines_iterator(&data) {
        if row_i == rows-1 do break
        row_i += 1
    }

    total := 0
    last_separator_i := 0 // not an entirely accurate name but whatever lol
    for s in fields_iterator(&data) {

        separator_i, found_separator := slice.linear_search(numbers[:], SEPARATOR)
        if !found_separator do separator_i = len(numbers)
        else do numbers[separator_i] = 0 // clear separator

        using math
        if s == "*" {
            total += prod(numbers[last_separator_i:separator_i])
        } else if s == "+" {
            total += sum(numbers[last_separator_i:separator_i])
        }
        assert(total >= 0, "should not overflow")

        last_separator_i = separator_i+1
    }
    fmt.println(total)
}
