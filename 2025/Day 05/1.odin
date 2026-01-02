package day_05

import "../common"
import "core:fmt"
import "core:strings"

Vector2 :: [2]int

main :: proc() {
    data := common.get_input_file_contents()

    fresh_ranges: [dynamic]Vector2
    in_fresh_part := true
    fresh_ids := 0

    for line in strings.split_lines_iterator(&data) {

        if len(line) == 0 {
            in_fresh_part = false
            continue
        }

        if in_fresh_part {
            s := strings.split(line, "-")
            start := common.parse_int(s[0])
            end   := common.parse_int(s[1])
            append(&fresh_ranges, Vector2{start, end})
        } else {
            id := common.parse_int(line)
            for range in fresh_ranges {
                if id >= range.x && id <= range.y {
                    fresh_ids += 1
                    break
                }
            }
        }
    }
    fmt.println(fresh_ids)
}

//
// linearly checking each id against each range should be fast enough, there's
// only 1000 ids and 182 ranges, and checking the range is cheap.  in the next
// part of the puzzle the requirements will probably change, so it's best to
// keep it simple.
//
