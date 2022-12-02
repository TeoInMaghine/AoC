allLines = []
with open('2021\\Day 2\\input.txt') as f:
    allLines = f.readlines()

x, y = 0, 0

for line in allLines:
    arguments = line.split()
    order = arguments[0]
    amount = int(arguments[1])

    if order == "forward":
        x += amount
    elif order == "up":
        y += amount
    elif order == "down":
        y -= amount

depth = -y

print(depth * x)