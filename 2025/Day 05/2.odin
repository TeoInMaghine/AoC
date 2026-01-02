package day_05

import "../common"
import "core:fmt"
import "core:strings"
import "core:slice"

Vector2 :: [2]int

vec2_less :: proc(i, j: Vector2) -> bool { return i.x < j.x }

main :: proc() {
    data := common.get_input_file_contents()

    fresh_ranges: [dynamic]Vector2

    for line in strings.split_lines_iterator(&data) {
        (len(line) != 0) or_break

        s := strings.split(line, "-")
        start := common.parse_int(s[0])
        end   := common.parse_int(s[1])
        append(&fresh_ranges, Vector2{start, end})
    }

    // we first sort by the starts to ensure we combine everything correctly as
    // we go and we don't need more aditional passes
    slice.sort_by(fresh_ranges[:], vec2_less)

    for i in 0..<len(fresh_ranges)-1 {
        // use a pointer to be able to modify it directly
        range := &fresh_ranges[i]

        for j := i+1; j < len(fresh_ranges); {
            other := fresh_ranges[j]

            // there are several options:
            // - the ranges don't overlap: in this case we simply continue
            // - otherwise: use the minimum start and the maximum end between
            //   both ranges to create a combined range

            // if other's start or end value are inside the inclusive range,
            // there's overlap
            overlap  := other.x >= range.x && other.x <= range.y 
            overlap ||= other.y >= range.x && other.y <= range.y

            if !overlap {
                j += 1
                continue
            }

            // because we sorted it already, it's always range.x <= other.x,
            // there's no need for range.x = min(range.x, other.x)
            range.y = max(range.y, other.y)

            // this can be pretty slow, but we need to preserve order for the
            // algorithm to not require additional passes (tho maybe it's not
            // even that slow, since you can mem-copy and stuff)
            ordered_remove(&fresh_ranges, j)
        }
    }

    // debug ranges, none should overlap
    for i in 0..<len(fresh_ranges)-1 {
        // use a pointer to be able to modify it directly
        range := fresh_ranges[i]

        for j in i+1..<len(fresh_ranges) {
            other := fresh_ranges[j]
            overlap := other.x >= range.x || other.y >= range.x
            overlap &&= other.x <= range.y || other.y <= range.y
            assert(!overlap, "there shouldn't be any overlapping ranges!")
        }
    }

    fresh_ids := 0
    for range in fresh_ranges {
        fresh_ids += range.y - range.x + 1
        assert(fresh_ids >= 0, "there was overflow")
    }

    fmt.println(fresh_ids)
}

//
// thank god I didn't overcomplicate it in the first part lol.
//
// I think I can do an N^2 (at most) check of the ranges that overlap and
// combine them if needed.  then, count how many fresh IDs are included in each
// range (end - start + 1, since it's an inclusive range).
//
