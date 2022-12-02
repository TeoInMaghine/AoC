import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

allLines = list(map(list, map(str.strip, allLines)))
allLines = [list(map(int, line)) for line in allLines]

def Vecinos(y, x):
    vecinos = []

    if y > 0:
        vecinos.append((y - 1, x))
    if y < (len(allLines) - 1):
        vecinos.append((y + 1, x))
    if x > 0:
        vecinos.append((y, x - 1))
    if x < (len(allLines[0]) - 1):
        vecinos.append((y, x + 1))
    
    return vecinos

vecinos = [[Vecinos(y, x) for x, height in enumerate(line)] for y, line in enumerate(allLines)]


lowestPoints = [] # (y, x)
for y, line in enumerate(allLines):
    for x, height in enumerate(line):
        if all([allLines[y][x] > height for y, x in vecinos[y][x]]):
            lowestPoints.append((y, x))

# print(lowestPoints)

def ProcessOpenSet():
    global openSet, processed, basin

    if not openSet: return

    newOpenSet = []
    for y, x in openSet[:]:
        if allLines[y][x] == 9 or processed[y][x]: continue
        basin.append((y, x))
        newOpenSet.extend(vecinos[y][x])
        processed[y][x] = True
    openSet = newOpenSet
    
    ProcessOpenSet()

basins = []
for lowPoint in lowestPoints:
    y, x = lowPoint
    basin = [lowPoint]
    openSet = [v for v in vecinos[y][x]]
    processed = [[False for height in line] for line in allLines]
    processed[y][x] = True

    ProcessOpenSet()
    basins.append(basin)

basins = list(map(len, basins))
basins.sort()
output = 1
for i in basins[-3:]: output *= i
print(output)