import os
# import heapq

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

count = 0
elvesGroup = []
sum = 0

def PriorityDetermination():
    global sum, count, elvesGroup

    itemType = elvesGroup[0].intersection(elvesGroup[1]).intersection(elvesGroup[2]).pop()
    priority = ord(itemType) - (96 if itemType.islower() else 38)
    print(itemType, priority)
    sum += priority

    count = 0
    elvesGroup = []

for line in allLines:
    count += 1

    elvesGroup.append(set(line.strip()))    
    if count >= 3:
        PriorityDetermination()

print(sum)