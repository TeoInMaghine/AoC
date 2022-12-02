allLines = []
with open('2021\\Day 1\\input.txt') as f:
    allLines = f.readlines()

previousMeasurment = None
increased = 0

for line in allLines:
    measurment = int(line)
    if previousMeasurment is not None and previousMeasurment < measurment:
        increased += 1
        
    previousMeasurment = measurment

print(increased)