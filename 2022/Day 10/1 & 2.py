import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

answ = ""
X = 1
cycle = 1
def GetCRTPixel():
    pixel = '#' if (X - 1 <= (cycle % 40 - 1) <= X + 1) else '.'
    if cycle % 40 == 0: pixel += '\n'
    return pixel

for line in allLines:
    answ += GetCRTPixel()
    if line.startswith("noop"):
        cycle += 1
    else:
        number = int(line.split()[1])
        cycle += 1        
        answ += GetCRTPixel()
        cycle += 1        
        X += number
    
print(answ)