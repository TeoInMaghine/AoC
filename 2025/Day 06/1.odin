package day_06

import "../common"
import "core:fmt"
import "core:strings"
import "core:math"

main :: proc() {
    data := common.get_input_file_contents()
    last_line_i := strings.count(data, common.newline)

    first_line := data[:strings.index(data, common.newline)]
    ss := strings.split(first_line, " ")
    cols := 0
    for s in ss {
        if len(s) == 0 do continue
        cols += 1
    }

    numbers := make([dynamic][dynamic]int, cols)
    rows := last_line_i
    for col in 0..<cols {
        numbers[col] = make([dynamic]int, rows)
    }

    i := 0
    for line in strings.split_lines_iterator(&data) {
        ss := strings.split(line, " ")

        if last_line_i == i {
            total := 0

            col := 0
            for s in ss {
                if len(s) == 0 do continue

                if s == "*" {
                    total += math.prod(numbers[col][:])
                } else if s == "+" {
                    total += math.sum(numbers[col][:])
                }
                assert(total >= 0, "it should not overflow")
                col += 1
            }

            fmt.println(total)
            break
        }

        row := i
        col := 0
        for s in ss {
            if len(s) == 0 do continue
            numbers[col][row] = common.parse_int(s)
            col += 1
        }

        i += 1
    }
}
