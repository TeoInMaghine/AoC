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
            s_pos = r, c

both_current_pos_dir = []
pipe_neighbours = get_pipe_neighbours(*s_pos)
for r, c, pipe in pipe_neighbours:
    pipe_dirs = pipes_dirs[pipe]

    for index, dir in enumerate(pipe_dirs):
        goal_r = r - dir[0]
        goal_c = c + dir[1]
        if goal_r == s_pos[0] and goal_c == s_pos[1]:
            non_matching_dir_index = 1 - index
            both_current_pos_dir.append((r, c, pipe_dirs[non_matching_dir_index]))


print(both_current_pos_dir)
#print(grid[both_current_pos_dir[0][0]][both_current_pos_dir[0][1]])
#print(grid[both_current_pos_dir[1][0]][both_current_pos_dir[1][1]])

distance = 1
while not (both_current_pos_dir[0][0] == both_current_pos_dir[1][0] and both_current_pos_dir[0][1] == both_current_pos_dir[1][1]):
    new_both_current_pos_dir = []
    for r, c, dir in both_current_pos_dir:
        next_r = r - dir[0]
        next_c = c + dir[1]
        next_pipe = grid[next_r][next_c]

        pipe_dirs = pipes_dirs[next_pipe]
        for index, dir in enumerate(pipe_dirs):
            goal_r = next_r - dir[0]
            goal_c = next_c + dir[1]
            
            if goal_r == r and goal_c == c:
                non_matching_dir_index = 1 - index
                new_both_current_pos_dir.append((next_r, next_c, pipe_dirs[non_matching_dir_index]))
    both_current_pos_dir = new_both_current_pos_dir

    distance += 1

print(distance)