import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

# First expand universe
newAllLines = []
for row in allLines:
    newAllLines.append(row)
    if '#' not in row.strip():
        newAllLines.append('.' * len(row.strip()))
allLines = list(newAllLines)

def insert (source_str, insert_str, pos):
    return source_str[:pos] + insert_str + source_str[pos:]

offset = 0
for c in range(len(allLines[0].strip())):
    column_has_galaxies = False
    for row in allLines:
        char = row[c]
        if char == '#':
            column_has_galaxies = True
    
    if not column_has_galaxies:
        for r, row in enumerate(newAllLines):
            newAllLines[r] = insert(row, '.', c + offset)

        offset += 1

allLines = newAllLines





# Then parse galaxies
galaxies = []
for r, row in enumerate(allLines):
    for c, char in enumerate(row.strip()):
        if char == '#':
            galaxies.append((r, c))
            

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