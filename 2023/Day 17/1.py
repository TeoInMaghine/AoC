import os
import heapq
import math

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

NORTH = 0
SOUTH = 1
WEST = 2
EAST = 3
opposite_dirs = {NORTH: SOUTH, SOUTH: NORTH, WEST: EAST, EAST: WEST}

# Considers consecutive tiles and directions
def is_in_bounds(x, y, origin_dir, origin_cons, dest_dir):
    # This is a very hacky way to get the consecutive tiles in init_base_neighbours working
    global hacky_cons

    # Don't allow 180º turns
    if opposite_dirs[origin_dir] == dest_dir:
        return False

    # Don't allow going in the same direction more than 3 times
    if origin_dir == dest_dir:
        if origin_cons >= 2:
            return False
        else: hacky_cons = origin_cons + 1
    else: hacky_cons = 0
    
    # Don't allow going out of the grid bounds
    return y >= 0 and y < ROWS_COUNT and x >= 0 and x < COLS_COUNT

class Node():
    def __init__(self, heat_loss, pos_y, pos_x, travel_direction, consecutive_tiles):
        self.heat_loss = heat_loss
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.travel_direction = travel_direction
        self.consecutive_tiles = consecutive_tiles

        self.parent = None
    
        # Calculate heuristic score with manhattan distance
        self.h_score = abs(self.pos_y - ROWS_COUNT - 1) + abs(self.pos_x - COLS_COUNT - 1)
        # G-score and F-score are infinite by default
        self.g_score = math.inf
        self.f_score = math.inf
    
    # All the nodes need to be generated before doing these, deferred initialization
    def init_base_neighbours(self):
        # Get base neighbours
        self.neighbours = []
        if is_in_bounds(self.pos_x, self.pos_y - 1, self.travel_direction, self.consecutive_tiles, NORTH):
            self.neighbours.append(grid[self.pos_y - 1][self.pos_x][NORTH][hacky_cons])

        if is_in_bounds(self.pos_x, self.pos_y + 1, self.travel_direction, self.consecutive_tiles, SOUTH):
            self.neighbours.append(grid[self.pos_y + 1][self.pos_x][SOUTH][hacky_cons])

        if is_in_bounds(self.pos_x - 1, self.pos_y, self.travel_direction, self.consecutive_tiles, WEST):
            self.neighbours.append(grid[self.pos_y][self.pos_x - 1][WEST][hacky_cons])

        if is_in_bounds(self.pos_x + 1, self.pos_y, self.travel_direction, self.consecutive_tiles, EAST):
            self.neighbours.append(grid[self.pos_y][self.pos_x + 1][EAST][hacky_cons])
    
    # For the priority queue
    def __lt__(self, other):
        return self.f_score < other.f_score

    def __repr__(self):
        return f'({self.pos_y}, {self.pos_x}) {self.heat_loss} F:{self.f_score} G:{self.g_score}'

def reconstruct_path():
    chars_for_dirs = {NORTH: '^', SOUTH: 'v', WEST: '<', EAST: '>'}
    debug_grid = [['.' for c in row] for row in grid]
    n = current
    while n.parent != None:
        print(n)
        debug_grid[n.pos_y][n.pos_x] = chars_for_dirs[n.travel_direction]
        n = n.parent
    
    for row in debug_grid:
        string = ""
        for char in row:
            string += char
        print(string)
    print(current.g_score)

ROWS_COUNT = len(allLines)
COLS_COUNT = len(allLines[0]) - 1 # ignore \n

# Parse data:
# Crucible can only move at most 3 tiles in the same direction,
# so we make a graph that also includes that
grid = [[[[Node(int(char), row, col, dir, cons) for cons in range(3)] for dir in range(4)] for col, char in enumerate(line.strip())] for row, line in enumerate(allLines)]

# Initialize
for row in grid:
    for dirs in row: 
        for cons in dirs:
            for node in cons:
                node.init_base_neighbours()

start_nodes = (grid[0][0][dir][0] for dir in range(4))
open_set = []
for start_node in start_nodes:
    start_node.g_score = 0
    start_node.f_score = start_node.h_score
    open_set.append(start_node)

# A* algorithm
while len(open_set) > 0:
    # Get lowest F-score node and remove it from the open set
    current = heapq.heappop(open_set)

    # Print heat loss accumulated when the goal is reached
    if current.pos_x == COLS_COUNT - 1 and current.pos_y == ROWS_COUNT - 1:
        reconstruct_path()
        break
    
    # Find dat path bitch
    for neighbour in current.neighbours:
        tentative_g_score = current.g_score + neighbour.heat_loss
        if tentative_g_score < neighbour.g_score:
            neighbour.parent = current
            neighbour.g_score = tentative_g_score
            neighbour.f_score = tentative_g_score + neighbour.h_score
            
            if neighbour not in open_set:
                heapq.heappush(open_set, neighbour)