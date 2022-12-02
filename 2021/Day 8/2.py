import os
from typing import Pattern

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

def ReturnIntersect(a, b):
    isAString = type(a) == str
    if isAString: intersect = ""
    else: intersect = []

    for i in a:
        for j in b:
            if i == j:
                if isAString: intersect += i
                else: intersect.append(i)
    
    return intersect

allPatternsSegments = ((0, 1, 2, 4, 5, 6), (2, 5), (0, 2, 3, 4, 6), (0, 2, 3, 5, 6), (1, 2, 3, 5), (0, 1, 3, 5, 6), (0, 1, 3, 4, 5, 6), (0, 2, 5), tuple(i for i in range(7)), (0, 1, 2, 3, 5, 6))

# Ordenados por cantidad de segmentos de cada patrón
uniquePatterns = (1, 7, 4, 8)
nonUniquePatterns = (2, 3, 5, 0, 6, 9)
uniquePatternsSegments = tuple(allPatternsSegments[i] for i in uniquePatterns) 
nonUniquePatternsSegments = tuple(allPatternsSegments[i] for i in nonUniquePatterns)

def SortSignalPatterns():
    newSignalPatterns = []
    for uPatternSegs in uniquePatternsSegments:
        lenght = len(uPatternSegs)
        for signalPattern in signalPatterns[:]:
            if lenght == len(signalPattern):
                newSignalPatterns.append(signalPattern)
                signalPatterns.remove(signalPattern)

    newSignalPatterns.extend(signalPatterns)
    return newSignalPatterns

def FirstStep():
    global segmentsConections
    processedPatterns = []

    uSignalPatterns = [p for p in signalPatterns if len(p) != 5 and len(p) != 6] 
    for pattern in uSignalPatterns:
        newPattern = str(pattern)

        for pPattern in processedPatterns:
            for signal in pPattern:
                newPattern = newPattern.replace(signal, "")

        for uPatternSegs in uniquePatternsSegments:
            if len(pattern) == len(uPatternSegs):
                for segment in uPatternSegs:
                    newSegmentConection = ReturnIntersect(segmentsConections[segment], newPattern)
                    if newSegmentConection: segmentsConections[segment] = newSegmentConection

        processedPatterns.append(pattern)

# Pasar por cada patrón no único
def SecondStep():
    global segmentsConections

    nUSignalPatterns = [p for p in signalPatterns if len(p) == 5 or len(p) == 6]
    for pattern in nUSignalPatterns:

        newSegmentsConections = {}        
        numberBeingFormed = []

        for i, segmentConections in enumerate(segmentsConections):
            # Si todas las letras de segmentConections están en el patrón, ignorar esa segmentConections (descartando las que no se pueden deducir)
            if len(ReturnIntersect(segmentConections, pattern)) != len(segmentConections):
                newSegmentsConections.setdefault(i, segmentConections)

            # Ver que número va formando, osea obtener los índices de los no-deducibles
            else:
                numberBeingFormed.append(i)            
        

        numbersThatFit = []
        patternsThatFit = []
        for i, nUPatternSegs in enumerate(nonUniquePatternsSegments):
            if len(nUPatternSegs) != len(pattern): continue
            if len(ReturnIntersect(numberBeingFormed, nUPatternSegs)) == len(numberBeingFormed):
                numbersThatFit.append(nonUniquePatterns[i])
                patternsThatFit.append(nUPatternSegs)

        for pThatFits in patternsThatFit:
            intersect = ReturnIntersect(pThatFits, newSegmentsConections.keys())
            newSegmentsConections = {i:newSegmentsConections[i] for i in intersect}

        for segmentConections in newSegmentsConections.items():
            key = segmentConections[0]
            intersect = ReturnIntersect(pattern, segmentConections[1])
            newSegmentsConections[key] = segmentsConections[key] = intersect

            for i, s in enumerate(segmentsConections):
                if i == key: continue
                segmentsConections[i] = s.replace(intersect, "")

        if all(len(s) == 1 for s in segmentsConections): break

outputTotal = 0
for line in allLines:
    signalPatterns, outputValues = line.split("|")
    signalPatterns = signalPatterns.strip().split(" ")

    segmentsConections = ["abcdefg"] * 7

    signalPatterns = SortSignalPatterns()

    FirstStep()
    SecondStep()

    segmentsConections = {s:i for i, s in enumerate(segmentsConections)}
    outputValues = outputValues.strip().split(" ")
    output = ""
    for oValue in outputValues:
        pattern = []
        for c in oValue:
            pattern.append(segmentsConections[c])
        pattern.sort()
        
        for i, p in enumerate(allPatternsSegments):
            if p == tuple(pattern): output += str(i)
    
    output = int(output)
    outputTotal += output
    print(f"output: {output}")

print(f"outputTotal: {outputTotal}")