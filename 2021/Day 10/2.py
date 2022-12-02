import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()    

openingBrackets = {'(': ')', '{': '}', '[': ']', '<': '>'}
closingBracketsPoints = {')': 1,']': 2, '}': 3, '>': 4}

def IsOpening(bracket):
    return bracket in openingBrackets

def GetClosing(bracket):
    return openingBrackets[bracket]

def BracketPoints(bracket):
    return closingBracketsPoints[bracket]

def LineScore(line):
    expectedClosing = []
    for currentBracket in line:
        if IsOpening(currentBracket):
            expectedClosing.append(GetClosing(currentBracket))
        else:
            if expectedClosing[-1] != currentBracket:
                return False
            expectedClosing.pop(-1)

    score = 0
    for currentBracket in expectedClosing.__reversed__():
        score *= 5        
        score += BracketPoints(currentBracket)
    
    return score


scores = []
for line in allLines:
    line = line.strip()

    score = LineScore(line)
    if score is False: continue

    print(f"Current score: {score}")
    scores.append(score)

scores.sort()
middleIndex = int(len(scores)/2)
print(f"Winner score: {scores[middleIndex]}")