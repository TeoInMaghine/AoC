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
        vecinos.append(allLines[y - 1][x])
    if y < (len(allLines) - 1):
        vecinos.append(allLines[y + 1][x])
    if x > 0:
        vecinos.append(allLines[y][x - 1])
    if x < (len(allLines[0]) - 1):
        vecinos.append(allLines[y][x + 1])
    
    return vecinos

riskLevel = 0
for y, line in enumerate(allLines):
    for x, height in enumerate(line):
        if all([v > height for v in Vecinos(y, x)]):
            riskLevel += 1 + height

print(riskLevel)