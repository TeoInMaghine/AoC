import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

# /: to right -> to up ; to down -> to left ; to up -> to right ; to left -> to down
forward_slash = {(0, 1): (-1, 0), (1, 0): (0, -1), (-1, 0): (0, 1), (0, -1): (1, 0)}
# \: to right -> to down ; to down -> to right ; to up -> to left ; to left -> to up
backward_slash = {(0, 1): (1, 0), (1, 0): (0, 1), (-1, 0): (0, -1), (0, -1): (-1, 0)}

grid = [[char for char in line.strip()] for line in allLines]

ROWS_COUNT = len(grid)
COLS_COUNT = len(grid[0])

def out_of_bounds(y, x):
    return y < 0 or y >= COLS_COUNT or x < 0 or x >= ROWS_COUNT

def iteration():
    global beams

    new_beams = []
    for beam in beams:
        pos_y, pos_x, dir_y, dir_x = beam

        # Memoization
        if beam in memo: continue
        else: memo.add(beam)

        new_pos_y = pos_y + dir_y
        new_pos_x = pos_x + dir_x

        if out_of_bounds(new_pos_y, new_pos_x):
            continue

        new_char = grid[new_pos_y][new_pos_x]

        # No-change cases
        if new_char == '.' or (dir_x != 0 and new_char == '-') or (dir_y != 0 and new_char == '|'):
            new_beams.append((new_pos_y, new_pos_x, dir_y, dir_x))
        elif new_char == '|':
            new_beams.append((new_pos_y, new_pos_x, -1, 0))
            new_beams.append((new_pos_y, new_pos_x, 1, 0))
        elif new_char == '-':
            new_beams.append((new_pos_y, new_pos_x, 0, -1))
            new_beams.append((new_pos_y, new_pos_x, 0, 1))
        elif new_char == '/':
            new_dir_y, new_dir_x = forward_slash[(dir_y, dir_x)]
            new_beams.append((new_pos_y, new_pos_x, new_dir_y, new_dir_x))
        elif new_char == '\\':
            new_dir_y, new_dir_x = backward_slash[(dir_y, dir_x)]
            new_beams.append((new_pos_y, new_pos_x, new_dir_y, new_dir_x))
        else:
            print("Wtf")
        

    
    beams = new_beams

def get_energized():
    global memo
    memo = set()

    energized = [[False for char in line.strip()] for line in allLines]

    while len(beams) > 0:
        iteration()

        for pos_y, pos_x, dir_y, dir_x in beams:
            energized[pos_y][pos_x] = True

    result = 0
    for row in energized:
        string = ""
        for is_energized in row:
            result += is_energized
            string += '#' if is_energized else '.'
        # print(string)

    return result

result = 0
for i in range(COLS_COUNT):
    # Top row
    beams = [(-1, i, 1, 0)]
    result = max(get_energized(), result)

    # Bottom row
    beams = [(ROWS_COUNT, i, -1, 0)]
    result = max(get_energized(), result)

for i in range(ROWS_COUNT):
    # Leftmost column
    beams = [(i, -1, 0, 1)]
    result = max(get_energized(), result)

    # Rightmost column
    beams = [(i, COLS_COUNT, 0, -1)]
    result = max(get_energized(), result)

print(result)