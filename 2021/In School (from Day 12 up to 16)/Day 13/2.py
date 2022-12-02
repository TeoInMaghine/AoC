with open('input.txt', 'r') as file:
    allLines = file.read().splitlines()

def PrintPaper():
    CreatePaper()
    print()
    
    numberOfPoints = 0
    for line in paper:
        l = ""
        for node in line:
            if node == '#': numberOfPoints += 1
            l += node
        print(l)
    
    # print(f"Number of points: {numberOfPoints}")


def CreatePaper():
    global paper
    paper = [[' ' for x in range(maxX)] for y in range(maxY)]
    
    for point in points:
        if point[0] >= 0 and point[1] >= 0:
            paper[point[1]][point[0]] = '#'        

def FoldPaper(axis, foldingLine):
    foldingMagicNumber = foldingLine * 2

    for point in points:
        if point[axis] > foldingLine:
            point[axis] = foldingMagicNumber - point[axis]
    
    global maxX, maxY
    if axis == 0: maxX = foldingLine
    else: maxY = foldingLine

foldingInstructions = False
points = []
maxX, maxY = 0, 0

for line in allLines:
    if len(line) == 0:
        foldingInstructions = True
        continue

    if not foldingInstructions:
        point = list(int(axis) for axis in line.split(','))
        points.append(point)
        maxX = max(maxX, point[0] + 1)
        maxY = max(maxY, point[1] + 1)
    else:
        split = line.split('=')
        FoldPaper(int(split[0][-1] == 'y'), int(split[1]))

PrintPaper()