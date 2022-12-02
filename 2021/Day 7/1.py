import os, math

line = ""
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    line = f.readline().strip()

crabPositions = list(map(int, line.split(",")))

# minimumFuelSpent = min([sum(abs(crab - i) for crab in crabPositions) for i in range(max(crabPositions))])

minimumFuelSpent = math.inf
minPosition = None
for i in range(max(crabPositions)):

    fuelSpent = 0
    for crab in crabPositions:
        fuelSpent += abs(crab - i)

    if fuelSpent < minimumFuelSpent:
        minimumFuelSpent = fuelSpent
        minPosition = i

print(minimumFuelSpent)
print(minPosition)