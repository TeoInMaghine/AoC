import os, math

line = ""
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    line = f.readline().strip()

crabPositions = list(map(int, line.split(",")))
crabPositions.sort() # para que la recursión no se cague en FuelSpent

maxCrabPosition = max(crabPositions)
fuelSpentTable = [None] * (maxCrabPosition + 1)
fuelSpentTable[0] = 0
fuelSpentTable[1] = 1

def FuelSpent(moveAmount):
    if fuelSpentTable[moveAmount] != None: return fuelSpentTable[moveAmount]

    fuelSpent = FuelSpent(moveAmount - 1) + moveAmount

    fuelSpentTable[moveAmount] = fuelSpent
    return fuelSpent

print(len(crabPositions) * maxCrabPosition)

minimumFuelSpent = math.inf
minPosition = None
for i in range(maxCrabPosition):

    fuelSpent = 0
    for crab in crabPositions:
        fuelSpent += FuelSpent(abs(crab - i))

    if fuelSpent < minimumFuelSpent:
        minimumFuelSpent = fuelSpent
        minPosition = i

print(minimumFuelSpent)
print(minPosition)