import os
# import heapq

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

sum = 0
for line in allLines:
    elves = line.strip().split(',')

    a1, a2 = elves[0].split('-')
    b1, b2 = elves[1].split('-')
    a1, a2, b1, b2 = int(a1), int(a2) + 1, int(b1), int(b2) + 1
    A, B = set(range(b1, b2)), set(range(a1, a2))

    sum += len(A & B) > 0
    print(sum)

print(sum) 