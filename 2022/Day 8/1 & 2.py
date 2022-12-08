import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

def PosToPosAndTrees(posList):
    return [grid[pos[1]][pos[0]] for pos in posList]

def GetTreesInEachDirection(column, row):
    columnsRight = [c for c in range(column + 1, len(grid))]
    rowsDown = [r for r in range(row + 1, len(grid))]
    columnsLeft = [c for c in range(column)]    
    rowsUp = [r for r in range(row)]

    columnsLeft.reverse()
    rowsUp.reverse()

    right = (list(zip(columnsRight, [row]*len(columnsRight))))
    down = (list(zip([column]*len(rowsDown), rowsDown)))
    left = (list(zip(columnsLeft, [row]*len(columnsLeft))))
    up = (list(zip([column]*len(rowsUp), rowsUp)))

    return PosToPosAndTrees(right), PosToPosAndTrees(down), PosToPosAndTrees(left), PosToPosAndTrees(up)

def ViewingDistance(treeValue, direction):
    distance = 0
    for tree in direction:
        distance += 1
        if tree >= treeValue:
            return distance
    
    return distance

grid = [[int(character) for character in line.strip()] for line in allLines]

highestScenicScore = 0
for column in range(len(grid) - 2):    
    for row in range(len(grid) - 2):

        treesInEachDirection = GetTreesInEachDirection(column + 1, row + 1)

        scenicScore = 1
        for direction in treesInEachDirection:
            scenicScore *= ViewingDistance(grid[row + 1][column + 1], direction)
        highestScenicScore = max(highestScenicScore, scenicScore)

print(highestScenicScore)