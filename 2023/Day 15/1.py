import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

steps = allLines[0].strip().split(',')

result = 0
for step in steps:
    current_value = 0

    for char in step:
        ascii = ord(char)
        current_value += ascii
        current_value *= 17
        current_value %= 256

    result += current_value

print(result)