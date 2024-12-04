import os
import re

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

N = len(allLines)

mas = ('M', 'A', 'S')
sam = ('S', 'A', 'M')

total = 0
for i in range(N):
    for j in range(N):
        current = allLines[i][j]
        if current == 'A':
            i_p = i + 1 < N
            i_n = i - 1 >= 0
            j_p = j + 1 < N
            j_n = j - 1 >= 0

            if i_p and i_n and j_p and j_n:
                inc = tuple(allLines[i-1+a][j-1+a] for a in range(3))
                dec = tuple(allLines[i-1+a][j+1-a] for a in range(3))
                total += (inc == sam and (dec == mas or dec == sam)) or (inc == mas and (dec == mas or dec == sam))


print(total)
