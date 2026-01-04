// I re-wrote this first part to use the same approach as the second part

package day_07

import "../common"
import "core:fmt"
import "core:strings"

main :: proc() {
    using common
    data := get_input_file_contents()

    width  := strings.index(data, newline)
    height := strings.count(data, newline) + 1
    line_length := width + len(newline)

    // beams always advance one row at a time on each iteration, so we can
    // process them by column
    beams := make([dynamic]bool, width)
    split_count := 0

    for row in 0..<height {
        for col in 0..<width {
            // data is an ASCII string, so we can access it by byte
            tile := data[row*line_length + col]

            switch tile {
            case '.':
                // carry beams to the next row or do nothing, so do nothing xd
            case 'S':
                // the first row only has the starting beam, so we process it
                // and skip the rest
                beams[col] = true; break
            case '^':
                /*

                when there's a splitter and there's a beam, we grab the beam in
                the current column and split it to the columns immediately to
                the left and right of it, and reset the current column.

                */
                if !beams[col] do continue
                beams[col-1] = true
                beams[col+1] = true
                beams[col] = false
                split_count += 1
            }
        }
    }

    fmt.println(split_count)
}
