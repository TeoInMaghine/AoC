import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

def HeadAndTailAreTouching(a):
    return abs(a[0]) <= 1 and abs(a[1]) <= 1

def PrintGrid():
    for row in grid:
        txt = ""
        for node in row:
            if node in knots:
                n = knots.index(node)
                if n == 0:
                    txt += 'H'
                else:
                    txt += str(n)
            elif node == start:
                txt += 's'
            elif node in visited:
                txt += '#'
            else:
                txt += '.'
        print(txt)
    print()

def FollowHead(head, tail, isLastTail):
    headMinusTail = (head[0] - tail[0], head[1] - tail[1])
    if HeadAndTailAreTouching(headMinusTail):
        return tail

    if headMinusTail[0] == 0:        
        tail = (tail[0], tail[1] + headMinusTail[1] - (1 if headMinusTail[1] > 0 else -1))
    elif headMinusTail[1] == 0:
        tail = (tail[0] + headMinusTail[0] - (1 if headMinusTail[0] > 0 else -1), tail[1])
    elif headMinusTail[0] == headMinusTail[1]:
        # This line f-ed mi up pretty hard, gave me an error of 5 with the actual input but none in the example
        # Basically I did "- 1" instead of "- (1 if headMinusTail[0] > 0 else -1)"
        # Used someone elses code to get the actual answer first so I could be sure I had a bug

        tail = (tail[0] + (headMinusTail[0] - (1 if headMinusTail[0] > 0 else -1)), tail[1] + (headMinusTail[1] - (1 if headMinusTail[1] > 0 else -1)))
    else:
        headMinusTail = (int(headMinusTail[0] / abs(headMinusTail[0])), int(headMinusTail[1] / abs(headMinusTail[1])))
        tail = (tail[0] + headMinusTail[0], tail[1] + headMinusTail[1])
    
    if isLastTail: visited.add(tail)

    return tail

grid = [[(row, column) for column in range(26)] for row in range(21)]
directions = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}

start = (15, 11)

knots = [start] * 10
visited = set()
visited.add(start)

for line in allLines:
    direction, times = line.split()  
    times = int(times)
    direction = directions[direction]    

    for t in range(times):
        knots[0] = (knots[0][0] + direction[0], knots[0][1] + direction[1])
        for i in range(1, 10):
            knots[i] = FollowHead(knots[i - 1], knots[i], i == 9)

# PrintGrid()
print(len(visited))