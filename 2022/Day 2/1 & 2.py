import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

def RoundResultScore(myShape):
    if myShape == 'X':
        return 0
    elif myShape == 'Y':
        return 3
    else:
        return 6

def RoundShapeChosenScore(oponentShape, myShape):
    if oponentShape == 'A':
        if myShape == 'X':
            return 3
        elif myShape == 'Y':
            return 1
        else:
            return 2
    if oponentShape == 'B':
        if myShape == 'X':
            return 1
        elif myShape == 'Y':
            return 2
        else:
            return 3
    if oponentShape == 'C':
        if myShape == 'X':
            return 2
        elif myShape == 'Y':
            return 3
        else:
            return 1

sum = 0
for round in allLines:
    oponentShape, myShape = round.strip().split()
    sum += RoundResultScore(myShape) + RoundShapeChosenScore(oponentShape, myShape)

print(sum)