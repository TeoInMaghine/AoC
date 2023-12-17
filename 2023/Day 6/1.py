import os
import math

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

times = allLines[0].removeprefix("Time:      ")
times = [int(time) for time in times.split()]

distances = allLines[1].removeprefix("Distance:  ")
distances = [int(distance) for distance in distances.split()]

result = 1
races_count = len(times)
for race_index in range(races_count):
    total_time = times[race_index]
    prev_record = distances[race_index]

    t1 = (-total_time + math.sqrt(total_time*total_time - 4*prev_record)) / -2
    t2 = (-total_time - math.sqrt(total_time*total_time - 4*prev_record)) / -2

    t1 = math.ceil(t1)
    t2 = math.floor(t2)
    dist_between_limits = t2 - t1
    print(t1, t2)

    distance_traveled = -(t1*t1) + total_time*t1
    if distance_traveled <= prev_record:
        dist_between_limits -= 1
    else:
        dist_between_limits += 1

    result *= dist_between_limits
    print(dist_between_limits)

print(result)