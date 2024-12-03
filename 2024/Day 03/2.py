import os
import re
from math import prod

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()


result = 0
mult = True
for line in allLines:
    matches = [m for m in re.finditer( r'mul\((\d)+,(\d)+\)', line)]
    for m in re.finditer( r'(do\(\))|(don\'t\(\))', line):
        matches.append(m)
    matches.sort(key=lambda m: m.span()[0])

    for m in matches:
        match = m.group()
        if match == "do()":
            mult = True
        elif match == "don't()":
            mult = False
        elif mult:
            result += prod(map(int, match[4:-1].split(',')))

print(result)
