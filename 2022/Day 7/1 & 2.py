import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

def Process(line):
    global ls, currentDir

    splitLine = line.split()
    if splitLine[0] == '$':
        ls = False
        if splitLine[1] == "ls":
            ls = True            
        elif splitLine[1] == "cd":
            if splitLine[2] == "..":
                currentDir = currentDir[:currentDir.rfind('/')]
                return


            directory = splitLine[2]
            if directory != '/':
                currentDir += '/'
            currentDir += directory
            directories[currentDir] = [0, []]
          
    else:
        if ls:
            if splitLine[0] == "dir":
                directories[currentDir][1].append(splitLine[1])
            else:
                directories[currentDir][0] += int(splitLine[0])

def RawProcessing(directory):    
    sum = 0
    for dir in directories[directory][1]:
        sum += RawProcessing(directory + "/" + dir)
    directories[directory][0] += sum

    return directories[directory][0]

def Solve():
    dirToDeleteMinSize = 30000000 - (70000000 - directories['/'][0])
    print(dirToDeleteMinSize)

    rawValues = list(directories[dir][0] for dir in directories)
    rawValues.sort()

    for value in rawValues:
        if value >= dirToDeleteMinSize:
            return value

ls = False
directories = {}
currentDir = ""

for line in allLines:
    Process(line)
RawProcessing('/')
print(Solve())