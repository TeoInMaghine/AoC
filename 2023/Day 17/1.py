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

class Node():
    def __init__(self, heat_loss, pos_y, pos_x, travel_direction):
        self.heat_loss = heat_loss
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.travel_direction = travel_direction

        self.parent = None
    
        # Calculate heuristic score with manhattan distance
        self.h_score = abs(self.pos_y - ROWS_COUNT - 1) + abs(self.pos_x - COLS_COUNT - 1)
        # G-score and F-score are infinite by default
        self.g_score = math.inf
        self.f_score = math.inf

        # Crucible can only move at most 3 tiles in the same direction
        # To take that into account, we store the consecutive tiles traveled in the same direction
        self.consecutive_tiles = 0
    
    # All the nodes need to be generated before doing these, deferred initialization
    def init_base_neighbours(self):
        # Get base neighbours
        self.neighbours = {}
        if self.pos_y - 1 >= 0 and self.pos_y - 1 < ROWS_COUNT:
            self.neighbours[NORTH] = grid[self.pos_y - 1][self.pos_x][NORTH]
        if self.pos_y + 1 >= 0 and self.pos_y + 1 < ROWS_COUNT:
            self.neighbours[SOUTH] = grid[self.pos_y + 1][self.pos_x][SOUTH]
        if self.pos_x - 1 >= 0 and self.pos_x - 1 < COLS_COUNT:
            self.neighbours[WEST] = grid[self.pos_y][self.pos_x - 1][WEST]
        if self.pos_x + 1 >= 0 and self.pos_x + 1 < COLS_COUNT:
            self.neighbours[EAST] = grid[self.pos_y][self.pos_x + 1][EAST]
    
    # For the priority queue
    def __lt__(self, other):
        return self.f_score < other.f_score

    def __repr__(self):
        return f'({self.pos_y}, {self.pos_x}) {self.heat_loss} F:{self.f_score} G:{self.g_score}'

def reconstruct_path():
    debug_grid = [['.' for c in row] for row in grid]
    n = current
    while n != None:
        print(n)
        debug_grid[n.pos_y][n.pos_x] = '#'
        n = n.parent
    
    for row in debug_grid:
        string = ""
        for char in row:
            string += char
        print(string)
    print(current.g_score)

ROWS_COUNT = len(allLines)
COLS_COUNT = len(allLines[0]) - 1 # ignore \n

# Parse data
# Columns and rows like always, but also cardinal directions to have the same node with different travel directions in the open set
grid = [[[Node(int(char), row, col, i) for i in range(4)] for col, char in enumerate(line.strip())] for row, line in enumerate(allLines)]

# Initialize
for row in grid:
    for dirs in row: 
        for node in dirs:
            node.init_base_neighbours()

start_nodes = (grid[0][0][i] for i in range(4))
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
    for direction, neighbour in current.neighbours.items():
        # Discard neighbour when going more than 3 times in the same direction
        if current.consecutive_tiles > 3 and direction == current.travel_direction:
            continue

        tentative_g_score = current.g_score + neighbour.heat_loss
        if tentative_g_score < neighbour.g_score:
            neighbour.parent = current
            neighbour.g_score = tentative_g_score
            neighbour.f_score = tentative_g_score + neighbour.h_score

            # neighbour.travel_direction = direction
            neighbour.consecutive_tiles = 2
            
            # Only reset consecutive tiles counter when changed direction
            if direction == current.travel_direction:
                neighbour.consecutive_tiles = current.consecutive_tiles + 1
            
            if neighbour not in open_set:
                heapq.heappush(open_set, neighbour)
            else:
                heapq.heapify(open_set)