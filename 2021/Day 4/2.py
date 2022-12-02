import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

drawnNumbers = allLines[0].split(",")
drawnNumbers[-1] = drawnNumbers[-1][:-1]
drawnNumbers = [int(n) for n in drawnNumbers]

boards = []
someBoard = []


for line in allLines[2:]:
    numbers = line.split()
    if not numbers: 
        boards.append(someBoard)
        someBoard = []
        continue
    
    someBoard.append([[int(n), False] for n in numbers]) 

wonBoards = [False for board in boards]

def PrintWinningScore(board, drawnNumber):
    sumOfUnmarked = 0
    for rows in board:
        for n in rows:
            if not n[1]:
                sumOfUnmarked += n[0]

    print(f"Final Score: {sumOfUnmarked * drawnNumber}")

def DrawNumbers():
    for drawnNumber in drawnNumbers:
        for boardIndex, board in enumerate(boards):
            for row in board:                
                for n in row:
                    if drawnNumber == n[0]:
                        n[1] = True
        
            if CheckIfWon(board, drawnNumber, boardIndex): return

def CheckIfWon(board, drawnNumber, boardIndex):

    for row in board:  
        won = True              
        for n in row:
            if n[1] == False:
                won = False

        if won:
            wonBoards[boardIndex] = True
            if all(wonBoards):
                PrintWinningScore(board, drawnNumber)
                return True

    columns = [list(e) for e in zip(*board)]
    for column in columns:
        won = True
        for n in column:
            if not n[1]:
                won = False
    
        if won:
            wonBoards[boardIndex] = True
            if all(wonBoards):
                PrintWinningScore(board, drawnNumber)
                return True
    
    return False

DrawNumbers()