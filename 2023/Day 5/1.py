import os

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
                seed_ranges.append(int(unprocessed_seeds[index + 1]))
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

def is_in_range(x, start, length):
    return start <= x and x < start + length

def process(current_map_index):
    global seed_ranges
    map = maps[current_map_index]

    for partial_map in map:
        map_start, _, map_length = partial_map
        new_seed_ranges = []
        for index, seed_start in enumerate(seed_ranges):
            if index % 2 != 0: continue

            seed_length = seed_ranges[index + 1]

            map_start_in_range = is_in_range(map_start, seed_start, seed_length)
            map_end_in_range = is_in_range(map_start + map_length - 1, seed_start, seed_length)

            print(map_start, seed_start, map_length)
            print(map_start_in_range, map_end_in_range)

            if map_start_in_range and map_end_in_range:
                if seed_start != map_start:
                    new_seed_ranges.append(seed_start)
                    first_length = map_start - seed_start
                    new_seed_ranges.append(first_length)
                
                new_seed_ranges.append(map_start)
                new_seed_ranges.append(map_length)

                if map_start + map_length != seed_start + seed_length:
                    last_start = map_start + map_length
                    last_length = seed_start + seed_length - last_start
                    new_seed_ranges.append(last_start)
                    new_seed_ranges.append(last_length)
            elif map_end_in_range:
                if map_start + map_length != seed_start + seed_length:
                    new_seed_ranges.append(seed_start)
                    first_length = map_start + map_length - seed_start
                    new_seed_ranges.append(first_length)
                
                    last_start = seed_start + first_length
                    last_length = seed_length - first_length
                    new_seed_ranges.append(last_start)
                    new_seed_ranges.append(last_length)
            elif map_start_in_range:
                if seed_start != map_start:
                    new_seed_ranges.append(seed_start)
                    first_length = map_start - seed_start
                    new_seed_ranges.append(first_length)

                    last_length = map_length - first_length
                    new_seed_ranges.append(map_start)
                    new_seed_ranges.append(last_length)
                else:
                    new_seed_ranges.append(seed_start)
                    new_seed_ranges.append(seed_length)
            else:
                new_seed_ranges.append(seed_start)
                new_seed_ranges.append(seed_length)

        seed_ranges = new_seed_ranges

    print(seed_ranges)
    # Convert to soil (at least in the first pass)
    for index, seed_start in enumerate(seed_ranges):
        if index % 2 != 0: continue

        for partial_map in map:
            map_start, map_destintation, map_length = partial_map
            offset = map_destintation - map_start

            seed_ranges[index] = seed_start + offset
    print(seed_ranges)


    current_map_index += 1
    seed_ranges = new_seed_ranges

    if current_map_index < len(maps):
        process(current_map_index)
    else:
        print("Result:")
        print(seed_ranges)

process(0)