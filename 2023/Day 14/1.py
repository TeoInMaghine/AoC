import os
import time

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

NORTH = (-1, 0)
WEST = (0, -1)
SOUTH = (1, 0)
EAST = (0, 1)

grid = [[char for char in line.strip()] for line in allLines]

ROW_COUNT = len(grid[0])
COLUMN_COUNT = len(grid)

def try_moving(pos, dir):
    global grid

    new_row, new_col = (pos[0] + dir[0], pos[1] + dir[1])

    out_of_bounds = new_row < 0 or new_row >= ROW_COUNT or new_col < 0 or new_col >= COLUMN_COUNT
    if out_of_bounds:
        return False
    
    # (I'll make sure I move the northest rocks first,
    # otherwise I would've needed recursion)
    char_in_dir = grid[new_row][new_col]
    if char_in_dir == '.':

        grid[new_row][new_col] = 'O'
        grid[pos[0]][pos[1]] = '.'

        return True
    
    return False

def tilt_in_dir(dir):
    moved = True
    while moved:
        moved = False

        for r, row in enumerate(grid):
            for c, char in enumerate(row):
                if char != 'O': continue

                # Try moving
                pos = r, c
                if try_moving(pos, dir):
                    moved = True

def print_grid():
    for row in grid:
        string = ""
        for char in row:
            string += char
        print(string)
    
    print()

def spin():
    tilt_in_dir(NORTH)
    tilt_in_dir(WEST)
    tilt_in_dir(SOUTH)
    tilt_in_dir(EAST)

def get_total_loads():
    total_loads = 0
    for r, row in enumerate(grid):
        for char in row:
            if char != 'O': continue

            load = ROW_COUNT - r
            total_loads += load
    
    return total_loads

# grids = {}
# cycle_start = 0
# cycle_length = 0
# for i in range(100):
    # spin()
    # hashable = str(grid)
    # if hashable not in grids:
        # grids[hashable] = i
    # else:
        # print("Found a cycle!")
        # cycle_start = grids[hashable]
        # cycle_length = i - cycle_start
        # break

# print(f"Cycle start: {cycle_start}")
# print(f"Cycle length: {cycle_length}")

cycle_start = 87
cycle_length = 9
TARGET = 1_000_000_000

equivalent = (TARGET - cycle_start) % cycle_length + cycle_start
print(equivalent)

for i in range(equivalent):
    spin()

result = get_total_loads()

print(result)

# print_grid()
