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

result = 0
configuration = [12, 13, 14]

for j, game in enumerate(games):
    is_possible = all([game[i] <= count for i, count in enumerate(configuration)])
    result += is_possible * (j + 1)

print(result)