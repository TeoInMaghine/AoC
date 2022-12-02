import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

matchingUniqueLengths = 0

for line in allLines:
    signalPatterns, outputValue = line.split("|")

    signalPatterns = signalPatterns.strip().split(" ")
    outputValue = outputValue.strip().split(" ")

    for pattern in outputValue:
        for uniqueLength in (2, 4, 3, 7):
            if len(pattern) == uniqueLength:
                matchingUniqueLengths += 1
                break

print(matchingUniqueLengths)