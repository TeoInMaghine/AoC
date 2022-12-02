import heapq

with open('input.txt', 'r') as file:
    allLines = file.read().splitlines()

length = len(allLines[0])
print(len(allLines[0]) == len(allLines))

class Node():
    parent = None
    fScore = float("inf")

    def __init__(self, pos, risk):
        self.pos = pos # y, x
        self.risk = risk
        self.gScore = float("inf")
        self.hScore = length - pos[0] + length - pos[1] - 2

    def __lt__(self, other):
        return self.fScore < other.fScore

    def CalculateVecinos(self):
        self.vecinos = []
        if self.pos[0] + 1 < len(grid):
            self.vecinos.append(grid[self.pos[0] + 1][self.pos[1]])
        if self.pos[1] + 1 < len(grid[0]):
            self.vecinos.append(grid[self.pos[0]][self.pos[1] + 1])
        if self.pos[0] - 1 >= 0:
            self.vecinos.append(grid[self.pos[0] - 1][self.pos[1]])
        if self.pos[1] - 1 >= 0:
            self.vecinos.append(grid[self.pos[0]][self.pos[1] - 1])

def risk_calculator(x, y):
    return (int(allLines[y % length][x % length]) - 1 + x // length + y // length) % 9 + 1

grid = [[Node((y, x), risk_calculator(x, y)) for x in range(length * 5)] for y in range(length * 5)]

for row in grid:
    a = ""
    for node in row:
        a += str(node.risk)
        if node.pos[1] == length - 1 and node.pos[0] < length:
            a += '|'
        node.CalculateVecinos()
    # print(a)

def AStar():
    openSet = [start]
    heapq.heapify(openSet)
    start.gScore = 0
    start.fScore = start.hScore
    
    while len(openSet) is not 0:
        current = heapq.heappop(openSet)

        if current is goal:
            return current.gScore

        for vecino in current.vecinos:
            tentative_gScore = current.gScore + vecino.risk
            if tentative_gScore < vecino.gScore:
                vecino.parent = current
                vecino.gScore = tentative_gScore
                vecino.fScore = tentative_gScore + vecino.hScore
                if vecino not in openSet:
                    heapq.heappush(openSet, vecino)

    return "bruh"

def path():
    current = goal
    total_path = [current.pos]
    while True:
        current = current.parent
        total_path.append(current.pos)
        if current is start:
            return total_path

start = grid[0][0]
goal = grid[length * 5 - 1][length * 5 - 1]

print(AStar())
# print(path())