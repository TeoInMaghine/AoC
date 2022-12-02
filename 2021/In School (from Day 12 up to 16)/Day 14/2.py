with open('input.txt', 'r') as file:
    allLines = file.read().splitlines()

polymer = allLines[0]

def MostCommonAndLeastCommon(string):
    # print(string)

    letters = {}
    for char in string:
        if char in letters: letters[char] += 1
        else: letters[char] = 1
    
    sortedConcurrences = sorted(list(letters.values()))
    print(sortedConcurrences[-1] - sortedConcurrences[0])

memo = {}
def ApplyRules(iterations, string):      
    global memo

    if iterations == 0: return string
    if (iterations, string) in memo: 
        return memo[iterations, string]

    stringToReturn = string[0]
    for i in range(len(string) - 1):
        one, two = string[i], string[i + 1]
        newTrio = one + rules[one + two] + two
        returnedString = ApplyRules(iterations - 1, newTrio)
        memo[iterations - 1, newTrio] = returnedString
        stringToReturn += returnedString[1:]
    
    return stringToReturn

rules = {line.split(" -> ")[0]: line.split(" -> ")[1] for line in allLines[2:]}
MostCommonAndLeastCommon(ApplyRules(40, polymer))
# print(memo)