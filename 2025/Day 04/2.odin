// Seems easy enough to "brute force", building on the solution of part 1

package day_04

import "../common"
import "core:fmt"
import "core:strings"

Vector2 :: [2]int

adjacent_directions :: [?]Vector2{
    {-1, -1},
    { 0, -1},
    { 1, -1},
    {-1,  0},
    // skip center
    { 1,  0},
    {-1,  1},
    { 0,  1},
    { 1,  1},
}


debug_print_neighs :: proc(neighs: [dynamic][dynamic]int) {
    RED :: "\033[01;31m"
    END :: "\033[00m"

    assert(len(neighs) > 0, "The neighbors dynamic array is empty")
    for row in 0..<len(neighs[0]) {
        for col in 0..<len(neighs) {
            fmt.print(neighs[col][row])
        }
        fmt.println()
    }
}

neigh_pos_in_bounds :: proc(pos: Vector2, width: int, height: int
    ) -> bool {
    return pos.x < width && pos.x >= 0 && pos.y < height && pos.y >= 0
}

main :: proc() {

    data := common.get_input_file_contents()
    width := strings.index(data, common.newline)
    height := strings.count(data, common.newline) + 1

    neighs := make([dynamic][dynamic]int, width, width)
    for &neigh_column in neighs {
        neigh_column = make([dynamic]int, height, height)
    }

    is_roll := make([dynamic][dynamic]bool, width, width)
    for &is_roll_column in is_roll {
        is_roll_column = make([dynamic]bool, height, height)
    }

    { // parse
        col := 0
        for line in strings.split_lines_iterator(&data) {
            for rune, row in line {
                is_roll[row][col] = rune == '@'
            }
            col += 1
        }
    }

    // calculate neighbor counts
    for neigh_column, row in neighs {
        for neigh, col in neigh_column {
            current_pos := Vector2{row, col}
            if is_roll[row][col] {
                for neigh_dir in adjacent_directions {
                    neigh_pos := current_pos + neigh_dir
                    neigh_pos_in_bounds(neigh_pos, width, height) or_continue
                    neighs[neigh_pos.x][neigh_pos.y] += 1
                }
            }
        }
    }

    // debug_print_neighs(neighs)

    removed_rolls := 0
    for {
        removed_roll_this_loop := false
        for neigh_column, row in neighs {
            for neigh, col in neigh_column {
                current_pos := Vector2{row, col}

                // remove roll if it's accessible
                if is_roll[row][col] && neigh < 4 {
                    for neigh_dir in adjacent_directions {
                        neigh_pos := current_pos + neigh_dir
                        neigh_pos_in_bounds(neigh_pos, width, height) or_continue
                        neighs[neigh_pos.x][neigh_pos.y] -= 1
                    }
                    is_roll[row][col] = false
                    removed_rolls += 1
                    removed_roll_this_loop = true
                }
            }
        }
        removed_roll_this_loop or_break
    }
    fmt.println(removed_rolls)
}
