import os
import math

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

seed_ranges = []
maps = []
current_map_index = 0

for i, line in enumerate(allLines):
    sline = line.strip()

    if i == 0:
        unprocessed_seeds = sline.split(" ")[1:]
        for index, element in enumerate(unprocessed_seeds):
            if index % 2 == 0:
                seed_ranges.append(int(element))
                seed_ranges.append(int(element) + int(unprocessed_seeds[index + 1]) - 1)
        continue
    if i == 1: continue

    if sline == "":
        current_map_index += 1
        continue

    if "-" in sline:
        maps.append([])
    else:
        partial_map = sline.split(" ")
        destination_start, source_start, range_length = [int(e) for e in partial_map]
        maps[current_map_index].append((source_start, destination_start, range_length))

print(maps)
print(seed_ranges)
