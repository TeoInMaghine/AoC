import time


with open('input.txt', 'r') as file:
    allLines = file.read().splitlines()

polymer = allLines[0]

def MostCommonAndLeastCommon():
    letters = {}
    for char in polymer:
        if char in letters: letters[char] += 1
        else: letters[char] = 1
    
    sortedConcurrences = sorted(list(letters.values()))
    print(sortedConcurrences[-1] - sortedConcurrences[0])


repetitions = 1
pairInsertionIterations = 15
times = [0 for i in range(pairInsertionIterations)]
for m in range(repetitions):
    polymer = allLines[0]
    
    for i in range(pairInsertionIterations):
        t0 = time.time()
        for pairInsertionRule in allLines[2:]:
            pair, add = pairInsertionRule.split(' -> ')
            result = f"{pair[0]}({add}){pair[-1]}"

            polymer = polymer.replace(pair, result)
            polymer = polymer.replace(pair, result)
            
        polymer = polymer.replace('(', '')
        polymer = polymer.replace(')', '')

        t1 = time.time()
        times[i] += t1 - t0

    # MostCommonAndLeastCommon()

times = [time / repetitions for time in times]
print(times[-1])
