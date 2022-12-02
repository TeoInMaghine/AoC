import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()    

class Octopus():
    def __init__(self, startingEnergy, row, column):
        self.energy = startingEnergy
        self.row = row
        self.column = column
        self.flashed = False
    
    def SetupVecinos(self):
        vecinos = []

        range = (-1, 0, 1)
        for i in range:
            row = i + self.row
            for j in range:
                if i == 0 == j: continue
                column = j + self.column

                if row < 0 or row >= len(grid): continue
                if column < 0 or column >= len(grid[0]): continue

                vecinos.append(grid[row][column])
        
        self.vecinos = vecinos
    
    def AddOneEnergy(self):
        if self.flashed: return

        self.energy += 1

        if self.energy > 9:
            global flashes
            flashes += 1
            self.flashed = True
            self.energy = 0

            for vecino in self.vecinos:
                vecino.AddOneEnergy()

def AddOneToAllOctopus():
    for octo in flatten_grid:
        octo.AddOneEnergy()

def ResetAllOctopus():
    for octo in flatten_grid:
        octo.flashed = False

def SetupAllVecinos():
    for octo in flatten_grid:
        octo.SetupVecinos()

def PrintStep(stepNumber):
    print(f"\nStep {stepNumber}\n")

    for i in grid:
        row = []
        for octo in i:
            row.append(octo.energy)
        print(row)

flashes = 0
grid = [[Octopus(int(allLines[row][column]), row, column) for column in range(len(allLines[0]) - 1)] for row in range(len(allLines))]
flatten_grid = [i for j in grid for i in j]
SetupAllVecinos()

def Main():
    for step in range(1000):
        prevFlashes = flashes

        AddOneToAllOctopus()

        if step == 194:
            print(prevFlashes, flashes)
        if prevFlashes + 100 == flashes:
            print(f"Sync flash at step: {step + 1}")
            return

        ResetAllOctopus()

Main()