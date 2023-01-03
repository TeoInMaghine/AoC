import os, time

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

class Monkey():

    def __init__(self, items, operation, testDivisible, trueMonkey, falseMonkey):
        self.items = items
        self.operation = operation
        self.testDivisible = testDivisible
        self.trueMonkey = trueMonkey
        self.falseMonkey = falseMonkey
    
    def ExecuteRoundActions(self):
        for index, item in enumerate(self.items):
            old = item
            start = time.time()
            self.items[index] = int(eval(self.operation) / 3)

            if self.items[index] % self.testDivisible:
                monkeys[self.trueMonkey].items.append(self.items[index])
            else:
                monkeys[self.falseMonkey].items.append(self.items[index])
        
        self.items = []


monkeys = []

for monkeyIndex in range(int((len(allLines) + 1) / 7)):
    ims = list(map(int, allLines[monkeyIndex * 7 + 1].removeprefix("  Starting items: ").removesuffix("\n").split(", ")))
    op = allLines[monkeyIndex * 7 + 2].removeprefix("  Operation: new = ").removesuffix("\n")
    testDiv = int(allLines[monkeyIndex * 7 + 3].removeprefix("  Test: divisible by "))
    fMonkey = int(allLines[monkeyIndex * 7 + 4].removeprefix("    If true: throw to monkey ").removesuffix("\n"))
    tMonkey = int(allLines[monkeyIndex * 7 + 5].removeprefix("    If false: throw to monkey ").removesuffix("\n"))

    monkey = Monkey(ims, op, testDiv, tMonkey, fMonkey)
    monkeys.append(monkey)

for round in range(1):
    for monkey in monkeys:
        monkey.ExecuteRoundActions()

for monkey in monkeys:
    print(monkey.items)