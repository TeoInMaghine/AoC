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

def process(seed_ranges, current_map_index):
    map = maps[current_map_index]
    new_seed_ranges = []

    for index, seed_start in enumerate(seed_ranges):
        if (index % 2) != 0: continue

        new_seed_ranges.append(seed_start)

        seed_end = seed_ranges[index + 1]

        for partial_map in map:
            map_start, _, range_length = partial_map

            # Add new ranges when map is inside range
            if seed_start < map_start and map_start < seed_end:
                new_seed_ranges.append(map_start - 1)
                new_seed_ranges.append(map_start)
            
        new_seed_ranges.append(seed_end)

    seed_ranges = new_seed_ranges
    new_seed_ranges = []

    for index, seed_start in enumerate(seed_ranges):
        if index % 2 != 0: continue

        new_seed_ranges.append(seed_start)

        seed_end = seed_ranges[index + 1]

        for partial_map in map:
            map_start, _, range_length = partial_map
            map_end = map_start + range_length - 1
            
            if seed_start < map_end and map_end < seed_end:
                new_seed_ranges.append(map_end)
                new_seed_ranges.append(map_end + 1)
            
        new_seed_ranges.append(seed_end)
    print(new_seed_ranges)


    # Convert seeds to soil (after the first conversion it's soil to fertilizer and so on)
    for index, seed in enumerate(new_seed_ranges):
        for partial_map in map:
            source_start, destination_start, range_length = partial_map
            offset = destination_start - source_start

            if (source_start <= seed) and (seed < source_start + range_length):
                seed += offset
                break
        
        new_seed_ranges[index] = seed

    print(new_seed_ranges)
    current_map_index += 1
    if current_map_index >= len(maps):
        print(f"result: {min(new_seed_ranges)}")
    else:
        process(new_seed_ranges, current_map_index)


# print(maps)
# print(seed_ranges)
# print()

current_map_index = 0
seed_ranges = [82, 92]
process(seed_ranges, current_map_index)

seed_ranges = [79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]
results =     [82, 83, 84, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 60, 86, 87, 88, 89, 94, 95, 96, 56, 57, 58, 59, 97, 98]