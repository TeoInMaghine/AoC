import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

def ElementsAreDifferent(list):
    return len(list) == len(set(list))

def Solve():
    marker = []
    i = 0
    for character in allLines[0]:
        marker.append(character)
        i += 1

        if len(marker) == 15:
            marker.pop(0)
            if ElementsAreDifferent(marker):
                return i
    
        # print(marker)

print(Solve())