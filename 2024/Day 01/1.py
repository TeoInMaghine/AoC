import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

left = []
right = {}
for line in allLines:
    l,r = map(int, line.split())
    left.append(l)
    if not l in right:
        right[l] = 0
    
    if not r in right:
        right[r] = 1
    else:
        right[r] += 1

print(sum(l * right[l] for l in left))
