import os

line = ""
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    line = f.readline()

fishes = list(map(int, line.split(",")))

for i in range(80):
    for i, fish in enumerate(fishes[:]):
        if fish == 0:
            fishes[i] = 6
            fishes.append(8)
        else:
            fishes[i] -= 1


print(len(fishes))