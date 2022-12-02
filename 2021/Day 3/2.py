import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

inputEntryLenght = len(allLines[0]) - 1
O = allLines[:]
CO2 = allLines[:]

for i in range(inputEntryLenght):
    ones = 0

    for number in O:
        if bool(int(number[i])): ones += 1

    oxygenCondition = ones >= len(O) / 2
    O[:] = [number for number in O if int(oxygenCondition) == int(number[i])]
    if len(O) == 1:
        break

for i in range(inputEntryLenght):
    ones = 0

    for number in CO2:
        if bool(int(number[i])): ones += 1

    co2Condition = ones < len(CO2) / 2
    CO2[:] = [number for number in CO2 if int(co2Condition) == int(number[i])]
    if len(CO2) == 1:
        break

print(int(O[0][:-1], 2) * int(CO2[0][:-1], 2))
