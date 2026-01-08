//
// > > to get the junction boxes closest to each other, we can simply iterate
// > > through all the pairs to figure that out, which is O(N^2).  since we
// > > have only 1000 junction boxes, it's fine.  the constant cost is not that
// > > much since we don't need to have the actual distance between them, the
// > > squared distance is enough to do comparisons.
//
// > > > then, to connect the n closest pairs, were n is 10 for the test input and
// > > > 1000 for the real input, we do the following:
// > > > 1. find the n closest connections and mark them in a bit array for
// > > >    connecting later.
//
// > > actually, I just realized this is not at all necessary, since there's only
// > > 1000 junction boxes in the real input, connecting the 1000 closest pairs
// > > just means iterating through all the points and connecting them to their
// > > closest point, lol.  kind of a trick-puzzle.
//
// > > (it'll be tricky to debug this with the test input, maybe I need to
// > > customize it or set the adjacency list manually or something)
//
// > > we can build an adjacency matrix to utilize a standard graph algorithm for
// > > finding the components (probably flood fill or something along those lines,
// > > which won't be more complex than O(N^2) for sure).  what we actually need
// > > for this part is the size of the 3 largest components.
//
// > > ...
//
// > > so, I will use this algorithm as a starting point:
// > > https://cp-algorithms.com/graph/search-for-connected-components.html.
// > > key consideration: I don't need to keep track of the points in the
// > > component, just how many points it contains.
//
// > oh no, I just realized I completely misinterpreted the problem statement:
// > the 10 (or in the case of the real problem, 1000) closest pairs CAN and WILL
// > have "repeated" points.  thankfully I think I just need to re-think the
// > first part of the solution, and can still re-use the
// > search-of-component-sizes part.
//
// okay there was an even bigger misinterpretation, because if two boxes are
// already part of the same circuit, then we don't do anything.  so you
// actually need to keep track of the circuits as you connect 'em up.
//
// anyhow there's some kind of bug, and this solution is already so convoluted
// that I don't wanna work with it anymore.  I'll try again some other time.
//

package day_08

import "../common"
import "core:fmt"
import "core:strings"
import "core:container/bit_array"
import "core:container/queue"
import "core:slice"

Vector3 :: [3]int

Connection :: struct {
    point_indices: [2]int,
    squared_distance: int,
}

connection_less :: proc(i,j: Connection) -> bool {
    return i.squared_distance < j.squared_distance
}

get_squared_distance :: proc(a, b: Vector3) -> int {
    diff_vector := a - b
    diff_vector *= diff_vector
    return diff_vector.x + diff_vector.y + diff_vector.z
}

main :: proc() {
    data := common.get_input_file_contents()

    // parse
    positions := strings.count(data, common.newline) + 1
    points := make([dynamic]Vector3, 0, positions)
    for line in strings.split_lines_iterator(&data) {
        ss := strings.split(line, ",")

        point: Vector3
        for s, j in ss do point[j] = common.parse_int(s)

        append(&points, point)
    }

    // calculate closest connections
    connections := make([dynamic]Connection, 0, positions*positions)
    for &point, i in points[:len(points)-1] {
        for &other, j_offset in points[i+1:] {
            j := i+1 + j_offset
            squared_distance := get_squared_distance(point, other)
            append(&connections, Connection{{i,j}, squared_distance})
        }
    }
    slice.sort_by(connections[:], connection_less)

    // adjacency matrix, utilizing the power of bit arrays to compress it quite
    // a lot.  a bit set in the (i,j) index means the i-th point connects with
    // the j-th point.
    adj := make([dynamic]bit_array.Bit_Array, positions)
    for &row, i in adj do bit_array.init(&row, positions)

    prev_components_count := 0
    connections_made := 0
    for connection in connections {
        using connection
        bit_array.set(&adj[point_indices.x], point_indices.y)
        bit_array.set(&adj[point_indices.y], point_indices.x)

        // find how many connected components the graph has
        components_count := 0

        visited_positions: bit_array.Bit_Array
        positions_to_process: queue.Queue(int)
        bit_array.init(&visited_positions, positions)
        queue.init(&positions_to_process, positions)

        it := bit_array.make_iterator(&visited_positions)
        for visited, i in bit_array.iterate_by_all(&it) {
            if !visited {
                component_size := 0
                queue.push_back(&positions_to_process, i)

                for queue.len(positions_to_process) > 0 {
                    current := queue.pop_back(&positions_to_process)
                    if !bit_array.get(&visited_positions, current) {
                        bit_array.set(&visited_positions, current)
                        component_size += 1

                        // add the connected positions to the processing stack
                        it := bit_array.make_iterator(&adj[i])
                        for index in bit_array.iterate_by_set(&it) {
                            queue.push_back(&positions_to_process, index)
                        }
                    }
                }

                components_count += 1
            }
        }

        // only count it as a connection if it changes how many components
        // there are
        if prev_components_count != components_count do connections_made += 1
        if connections_made == 10 do break

        prev_components_count = components_count
    }

    // find sizes of the connected components of the graph
    component_sizes := make([dynamic]int, 0, positions)

    visited_positions: bit_array.Bit_Array
    positions_to_process: queue.Queue(int)
    bit_array.init(&visited_positions, positions)
    queue.init(&positions_to_process, positions)

    it := bit_array.make_iterator(&visited_positions)
    for visited, i in bit_array.iterate_by_all(&it) {
        if !visited {
            component_size := 0
            queue.push_back(&positions_to_process, i)

            for queue.len(positions_to_process) > 0 {
                current := queue.pop_back(&positions_to_process)
                if !bit_array.get(&visited_positions, current) {
                    bit_array.set(&visited_positions, current)
                    component_size += 1

                    // add the connected positions to the processing stack
                    it := bit_array.make_iterator(&adj[i])
                    for index in bit_array.iterate_by_set(&it) {
                        queue.push_back(&positions_to_process, index)
                    }
                }
            }

            append(&component_sizes, component_size)
        }
    }

    slice.reverse_sort(component_sizes[:])
    fmt.println(component_sizes)
    fmt.println(component_sizes[0] * component_sizes[1] * component_sizes[2])
}
