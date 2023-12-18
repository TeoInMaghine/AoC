import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

pipes_dirs = {'|': (( 1, 0), (-1, 0)),
              '-': (( 0, 1), ( 0,-1)),
              'L': (( 0, 1), ( 1, 0)),
              'J': (( 0,-1), ( 1, 0)),
              'F': (( 0, 1), (-1, 0)),
              '7': (( 0,-1), (-1, 0))}

grid = [[c for c in line.strip()] for line in allLines]

column_count = len(grid[0])
row_count = len(grid)

def get_pipe_neighbours(r, c):
    neighbours = []

    if r != 0:
        pipe = grid[r-1][c]
        if pipe in pipes_dirs:
            neighbours.append((r-1, c, pipe))
    if r != row_count - 1:
        pipe = grid[r+1][c]
        if pipe in pipes_dirs:
            neighbours.append((r+1, c, pipe))
    if c != 0:
        pipe = grid[r][c-1]
        if pipe in pipes_dirs:
            neighbours.append((r, c-1, pipe))
    if c != column_count - 1:
        pipe = grid[r][c+1]
        if pipe in pipes_dirs:
            neighbours.append((r, c+1, pipe))

    return neighbours

# Find starting pos
for r, row in enumerate(grid):
    for c, obj in enumerate(row):
        if obj == 'S':
            start_pos = r, c

pipe_neighbours = get_pipe_neighbours(*start_pos)
for r, c, pipe in pipe_neighbours:
    pipe_dirs = pipes_dirs[pipe]

    for dir in pipe_dirs:
        goal_r = r - dir[0]
        goal_c = c + dir[1]
        if goal_r == start_pos[0] and goal_c == start_pos[1]:
            print("e")
