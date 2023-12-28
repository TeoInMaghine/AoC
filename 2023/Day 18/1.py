import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

dirs = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1),}

# Parse data
moves = []
for line in allLines:
    dir, move, color = line.split()
    moves.append((dirs[dir], int(move)))

holes = []
max_x = max_y = 0
x = y = 0
for dir, move in moves:
    mx, my = dir

    for i in range(move):
        holes.append((x, y))
        max_x = max(x, max_x)
        max_y = max(y, max_y)

        x += mx
        y += my

grid = []
for y in range(max_y + 1):
    grid.append([])
    for x in range(max_x + 1):
        if (x, y) in holes:
            i = holes.index((x, y))
            grid[y].append(i)
        else: grid[y].append(-1)

def get_vertical_neighbour_dir(i):
    local_dirs = []

    x, y = holes[i]
    if (y+1 <= max_y) and (grid[y+1][x] == (i+1) % len(holes) or grid[y+1][x] == (i-1) % len(holes)):
        local_dirs.append(dirs['D'])
    if (y-1 >= 0) and (grid[y-1][x] == (i+1) % len(holes) or grid[y-1][x] == (i-1) % len(holes)):
        local_dirs.append(dirs['U'])
    
    return local_dirs

new_holes = holes.copy()
for y, row in enumerate(grid):
    entry_dir = None
    walls = 0
    for x, hole in enumerate(row):
        if y == 0:
            print("bitch")
        if hole == -1:
            if walls % 2 != 0:
                new_holes.append((x, y))
            continue

        hole_vert_dirs = get_vertical_neighbour_dir(hole)
        if len(hole_vert_dirs) == 2:
            walls += 1
        elif len(hole_vert_dirs) == 1:
            if entry_dir == None:
                entry_dir = hole_vert_dirs[0]
            elif entry_dir != hole_vert_dirs[0]:
                walls += 1 
holes = new_holes


for j in range(max_y + 1):
    string = ""
    for i in range(max_x + 1):
        string += '#' if (i, j) in holes else '.'
    print(string)

print(len(holes))