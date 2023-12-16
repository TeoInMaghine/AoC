import os
import math

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

seeds = []
maps = []
current_map_index = 0

for i, line in enumerate(allLines):
    sline = line.strip()

    if i == 0:
        seeds = sline.split(" ")[1:]
        seeds = [int(e) for e in seeds]
        continue
    if i == 1: continue

    if sline == "":
        current_map_index += 1
        continue

    if "-" in sline:
        maps.append([])
        # Actually this is unnecessary lol, just in case I need it for
        # part 2 I'll keep it:
        sline = sline.removesuffix(" map:")
        source, _, destination = sline.split("-")
    else:
        partial_map = sline.split(" ")
        destination_start, source_start, range_length = [int(e) for e in partial_map]
        maps[current_map_index].append((source_start, destination_start, range_length))

print(maps)
result = math.inf
for seed in seeds:
    for map in maps:
        for partial_map in map:

            source_start, destination_start, range_length = partial_map
            offset = destination_start - source_start
            if (source_start <= seed) and (seed < source_start + range_length):
                seed += offset
                break

    # At this point it's a location
    print(seed)
    result = min(result, seed)


print(result)
