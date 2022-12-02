allLines = []
with open('2021\\Day 1\\input.txt') as f:
    allLines = f.readlines()

allLines = [int(line) for line in allLines]
threeMeasurmentList = [allLines[i] + allLines[i+1] + allLines[i+2] for i in range(len(allLines) - 2)]

previousMeasurment = None
increased = 0

for measurment in threeMeasurmentList:
    if previousMeasurment is not None and previousMeasurment < measurment:
        increased += 1        
    previousMeasurment = measurment

print(increased)