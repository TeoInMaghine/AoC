import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

NORTH = (-1, 0)

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

moved = True
while moved:
    moved = False

    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char != 'O': continue

            # Try moving
            pos = r, c
            if try_moving(pos, NORTH):
                moved = True


result = 0
for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char != 'O': continue

        load = ROW_COUNT - r
        result += load

print(result)