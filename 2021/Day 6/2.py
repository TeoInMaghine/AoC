import os

line = ""
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    line = f.readline()

fishes = list(map(int, line.split(",")))

daysToPass = 256

fishAmountTable = [None] * (daysToPass + 8)
def FishCreated(daysLeft):
    global fishAmountTable
    if fishAmountTable[daysLeft] != None:
        return fishAmountTable[daysLeft]

    fishAmount = 1
    for rawDaysLeft in range(daysLeft - 7, -1, -7):
        fishAmount += FishCreated(rawDaysLeft - 2)

    fishAmountTable[daysLeft] = fishAmount
    return fishAmount

print(sum([FishCreated(daysToPass + (6 - fish)) for fish in fishes[:]]))