allLines = []
with open('2021\\Day 2\\input.txt') as f:
    allLines = f.readlines()

x, y = 0, 0
aim = 0

for line in allLines:
    arguments = line.split()
    order = arguments[0]
    amount = int(arguments[1])

    if order == "forward":
        x += amount
        y += amount * aim
    elif order == "up":
        aim += amount
    elif order == "down":
        aim -= amount
    
    # print(f"x: {x}, y: {y}, aim: {aim}")

depth = -y
print(depth * x)