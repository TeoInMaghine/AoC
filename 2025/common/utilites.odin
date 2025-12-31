package common

import "core:os"
import "core:strings"

newline :: "\r\n" when ODIN_OS == .Windows else "\n"

get_input_file_contents :: proc() -> (data: string) {
    raw_data, ok := os.read_entire_file_from_filename("input.txt")
    assert(ok, "input.txt could not be read")

    data = string(raw_data)
    data = strings.trim_suffix(data, newline)

    return data
}
