with open('input.txt', 'r') as file:
    allLines = file.read().splitlines()

caveConnections = {}

def AddConnection(first, second):
    global caveConnections

    if first in caveConnections and second not in caveConnections[first]:
        caveConnections[first].append(second)
    else: caveConnections[first] = [second]

for line in allLines:
    first, second = line.split('-')

    AddConnection(first, second)
    AddConnection(second, first)

paths = 0
path = []
def AddCaveToPath(path, cave):
    global paths

    path.append(cave)
    for possibility in caveConnections[cave]:
        # print(possibility)
        if possibility == "end":
            path.append(possibility)
            # print(path)
            paths += 1
            continue
        elif possibility == "start":
            continue

        smallCave = possibility.islower()
        # print(not smallCave or possibility not in path)
        if not smallCave or possibility not in path:
            AddCaveToPath(path[:], possibility)

AddCaveToPath(path[:], "start")
print(paths)