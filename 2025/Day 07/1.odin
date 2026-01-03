package day_07

import "../common"
import "core:fmt"
import "core:strings"
import "core:container/queue"
import "core:container/bit_array"

main :: proc() {
    Vector2 :: [2]int

    LEFT  :: Vector2{ 0,-1}
    RIGHT :: Vector2{ 0, 1}
    DOWN  :: Vector2{ 1, 0}

    using common
    data := get_input_file_contents()

    width  := strings.index(data, newline)
    height := strings.count(data, newline) + 1
    line_length := width + len(newline)

    // I think I'll need at most width*2, but I don't want to resize or think
    // about it so I'll just allocate width*4
    beams: queue.Queue(Vector2)
    queue.init(&beams, width*4)

    // parse
    grid :=    make([dynamic][dynamic]u8,         height)
    visited := make([dynamic]bit_array.Bit_Array, height)
    for &row, i in grid {
        row = make([dynamic]u8, width)
        bit_array.init(&visited[i], 0, width)
        for &tile, j in row {
            // data is an ASCII string, so we can access it by byte
            tile = data[i*line_length + j]
            if tile == 'S' do queue.push_back(&beams, Vector2{i,j})
        }
    }

    // for row in 0..<height {
    //     for col in 0..<width {
    //         fmt.print(rune(grid[row][col]))
    //     }
    //     fmt.println()
    // }

    split_count := 0
    beam := queue.pop_front(&beams)
    ok := true

    for ; ok; beam, ok = queue.pop_front_safe(&beams) {
        current_tile := grid[beam.x][beam.y]
        if bit_array.get(&visited[beam.x], beam.y) do continue
        bit_array.set(&visited[beam.x], beam.y)

        if current_tile == '^' {
            split_count += 1
            queue.push_back_elems(&beams, beam+LEFT, beam+RIGHT)
            continue
        }

        if new_beam := beam+DOWN; new_beam.x < height {
            queue.push_back(&beams, new_beam)
        }
    }

    // for row in visited {
    //     fmt.printfln("%15b", row.bits)
    // }

    fmt.println(split_count)
}
