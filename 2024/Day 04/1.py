import os
import re

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

N = len(allLines)

xmas = tuple(('X', 'M', 'A', 'S'))

total = 0
for i in range(N):
    for j in range(N):
        current = allLines[i][j]
        if current == 'X':
            i_p = i + 3 < N
            i_n = i - 3 >= 0
            j_p = j + 3 < N
            j_n = j - 3 >= 0

            if i_p:
                total += xmas == tuple(allLines[i+a][j] for a in range(4))
                if j_p:
                    total += xmas == tuple(allLines[i+a][j+a] for a in range(4))
                if j_n:
                    total += xmas == tuple(allLines[i+a][j-a] for a in range(4))

            if i_n:
                total += xmas == tuple(allLines[i-a][j] for a in range(4))
                if j_p:
                    total += xmas == tuple(allLines[i-a][j+a] for a in range(4))
                if j_n:
                    total += xmas == tuple(allLines[i-a][j-a] for a in range(4))

            if j_p:
                total += xmas == tuple(allLines[i][j+a] for a in range(4))
            if j_n:
                total += xmas == tuple(allLines[i][j-a] for a in range(4))




print(total)
