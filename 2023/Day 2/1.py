import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

# Parse data first

# Contains max cubes show at a time of each color [r, g, b] in each game
games = []
for i, line in enumerate(allLines):

    sLine = line.strip()
    _ , sets = sLine.split(": ")
    sets = sets.split("; ")

    games.append([0, 0, 0])
    for set in sets:
        cubes_shown = set.split(", ")

        for color in cubes_shown:
            count, color = color.split(" ")

            index = 0 if color == "red" else 1 if color == "green" else 2
            games[i][index] = max(games[i][index], int(count))

print(games)

# Calculate power
result = 0

for r, g, b in games:
    result += r * g * b

print(result)