import os
import heapq as heap

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

caloriesPerElve = []
heap.heapify(caloriesPerElve)

caloriesSum = 0
for line in allLines:
    if line == '\n':
        heap.heappush(caloriesPerElve, caloriesSum)
        caloriesSum = 0
    else:
        caloriesSum += int(line.strip())

print(sum(heap.nlargest(3, caloriesPerElve)))