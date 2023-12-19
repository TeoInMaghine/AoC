import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

def column_has_no_galaxies(c):
    has_no_galaxies = True
    for row in allLines:
        char = row[c]
        if char == '#':
            has_no_galaxies = False
    
    return has_no_galaxies

EXPANSION_CONST = 1_000_000 - 1
galaxies = []

row_expansion = 0

for r, row in enumerate(allLines):
    column_expansion = 0
    for c, char in enumerate(row.strip()):
        if column_has_no_galaxies(c):
            print(f"column expansion: {c}")
            column_expansion += EXPANSION_CONST

        if char == '#':
            galaxies.append((r + row_expansion, c + column_expansion))

    if '#' not in row.strip():
        print("row expansion")
        row_expansion += EXPANSION_CONST
print(galaxies)

def get_manhattan_distance(pos_1, pos_2):
    x1, y1 = pos_1
    x2, y2 = pos_2

    return abs(x1 - x2) + abs(y1 - y2)

result = 0
for i, galaxy_a in enumerate(galaxies[:-1]):
    for galaxy_b in galaxies[i+1:]:
        result += get_manhattan_distance(galaxy_a, galaxy_b)

print(result)