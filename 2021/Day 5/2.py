import os, numpy as np

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

markedPoints = np.zeros([1000, 1000]).astype(int)

for line in allLines:

    firstData = line.replace(" -> ", ",").replace("\n", "").split(",")
    x1, y1, x2, y2 = list(map(int, firstData))
    dir = np.subtract([x2, y2], [x1, y1])

    normalizedDir = np.sign(dir)

    for i in range(max(abs(dir[0]), abs(dir[1])) + 1):
        index = [x1, y1] + normalizedDir * i        
        markedPoints[index[0], index[1]] += 1

print(np.flip(np.rot90(markedPoints, 1), 0))

intersectPoints = 0
for row in markedPoints:
    for i in row:
        if i >= 2: intersectPoints += 1

print(intersectPoints)
