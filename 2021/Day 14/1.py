import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

polymer = allLines[0].strip()
insertionRules = {}

for line in allLines[2:]:
    line = line.strip()
    pair, inserted = line.split(" -> ")

    insertionRules[pair] = (pair[0] + inserted, inserted + pair[1])

def Score():
    letters = {}

    for pair in pairs.keys():
        if pairs[pair] == 0: continue
        for letter in pair:
            if letter in letters:
                letters[letter] += pairs[pair]
            else:
                letters[letter] = pairs[pair]

    for key in letters.keys():
        if key == polymer[0] or key == polymer[-1]:
            letters[key] = 1 + ((letters[key] - 1) / 2)
        else: letters[key] /= 2
    
    mostCommon = max(letters.values())
    leastCommon = min(letters.values())
    print(f"Most: {mostCommon}, Least: {leastCommon}, Sum: {sum(letters.values())}, Score: {mostCommon - leastCommon}\n")

pairs = {}
for i in range(len(polymer) - 1):
    pair = polymer[i] + polymer[i+1]
    if pair in pairs: pairs[pair] += 1
    else: pairs[pair] = 1

for i in range(40):
    lastPairs = pairs.copy().items()

    for pair in lastPairs:
        if pair[1] == 0: continue
        newPairs = insertionRules[pair[0]]
        pairs[pair[0]] -= pair[1]
        for newPair in newPairs:
            if newPair in pairs:
                pairs[newPair] += pair[1]
            else: pairs[newPair] = pair[1]

Score()