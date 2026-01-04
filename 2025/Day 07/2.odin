// I love so much how simple this turned out that I think I'll rewrite the
// first part to use the same approach

package day_07

import "../common"
import "core:fmt"
import "core:strings"
import "core:math"

main :: proc() {
    using common
    data := get_input_file_contents()

    width  := strings.index(data, newline)
    height := strings.count(data, newline) + 1
    line_length := width + len(newline)

    // beams always advance one row at a time on each iteration, so we can
    // process them by column and naturally accumulate "timelines"
    beams := make([dynamic]int, width)

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
                beams[col] = 1; continue
            case '^':
                /*

                when there's a splitter we grab the beams in the current
                column and add them to the columns immediately to the left
                and right of it, and reset the current column.
                
                because there are never two splitters right next to each
                other, we don't have to worry about duplicating beams
                unnecessarily, so we don't need something like
                "current_beams" and "next_beams".

                */
                beams[col-1] += beams[col]
                beams[col+1] += beams[col]
                beams[col] = 0
            }
        }
    }

    fmt.println(math.sum(beams[:]))
}
