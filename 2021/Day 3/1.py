import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

inputEntryLenght = len(allLines[0]) - 1
gamma = 0
epsilon = 0

for i in range(inputEntryLenght):
    ones = 0
    for line in allLines:
        if bool(int(line[i])): ones += 1

    gammaDigit = int(ones > len(allLines) / 2)
    binaryOrder = 2 ** (inputEntryLenght - i - 1)

    gamma += gammaDigit * binaryOrder
    epsilon += int(not gammaDigit) * binaryOrder

print(gamma * epsilon)