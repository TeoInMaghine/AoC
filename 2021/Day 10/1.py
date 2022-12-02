import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()    

openingBrackets = {'(': ')', '{': '}', '[': ']', '<': '>'}
closingBracketsScore = {')': 3,']': 57, '}': 1197, '>': 25137}

def IsOpening(bracket):
    return bracket in openingBrackets

def GetClosing(bracket):
    return openingBrackets[bracket]

def Score(bracket):
    return closingBracketsScore[bracket]

score = 0
def LineCorruptionScore(line):
    expectedClosing = []
    for currentBracket in line:
        if IsOpening(currentBracket):
            expectedClosing.append(GetClosing(currentBracket))
        else:
            if expectedClosing[-1] != currentBracket:
                return Score(currentBracket)
            expectedClosing.pop(-1)
        
    global incomplete
    incomplete = len(expectedClosing) > 0

    return 0

score = 0
for line in allLines:
    line = line.strip()

    currentScore = LineCorruptionScore(line)
    score += currentScore

    if currentScore > 0: print(f"Corrupted line:\t{line}")
    # elif incomplete: print(f"Incomplete line:\t{line}")
    # else: print(f"Clean line:\t{line}")

print(f"Corruption score: {score}")