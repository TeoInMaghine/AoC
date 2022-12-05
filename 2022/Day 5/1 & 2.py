import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

instructions = False

stacks = [[] for i in range(9)]

for line in allLines:
    if line == "\n":
        instructions = True
        continue

    if not instructions:
        for i in range(int(len(line) / 4)):
            crate = line[i * 4 + 1]
            if crate.isspace() or crate.isdigit(): continue
            stacks[i].append(crate)
    else:
        processedLine = line[5:].replace("from ", "").replace("to ", "")
        crateCount, fromStack, toStack = map(int, processedLine.split())
        fromStack -= 1
        toStack -= 1

        newFromStack = stacks[fromStack][crateCount:]
        movedCrates = stacks[fromStack][:crateCount]
        # movedCrates.reverse() # literally the only difference between 1 & 2

        stacks[toStack][0:0] = movedCrates
        stacks[fromStack] = newFromStack

answ = ""
for stack in stacks:
    answ += stack[0]
print(answ)