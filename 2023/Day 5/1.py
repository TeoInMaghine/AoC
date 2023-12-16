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

# Increment location and mapping backwards 
# until getting a valid seed, that's the lowest location
def trace_back_to_seed(location):
    for map in maps:
        for partial_map in map:
            source_start, destination_start, range_length = partial_map

            # print(f"{destination_start} <= L: {location} < {destination_start + range_length} = {(destination_start <= location) and (location < destination_start + range_length)}")

            # Should map from destination to source instead of source to destination
            if (destination_start <= location) and (location < destination_start + range_length):
                offset = destination_start - source_start
                location -= offset

                break
                # print(f"Transf: {location}")
    
    # Now a seed
    return location

print(seed_ranges)

# Reverse every mapping's order
maps.reverse()
for i, map in enumerate(maps):
    map.reverse()
    maps[i] = map

print(maps)

location = 0
found_result = False
while(not found_result):
    seed = trace_back_to_seed(location)
    for i, seed_start in enumerate(seed_ranges):
        if i % 2 != 0: continue

        seed_end = seed_ranges[i + 1]
        if (seed_start <= seed) and (seed <= seed_end):
            found_result = True
            print(f"Result: {seed}")

    location += 1
