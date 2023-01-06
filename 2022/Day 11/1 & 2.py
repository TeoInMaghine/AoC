import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

mod_constant = 17 * 19 * 7 * 11 * 13 * 3 * 5 * 2

# I had to look in the AoC subreddit to solve part 2 of the puzzle,
# because I didn't know this mathematical theorem (Chinese remainder theorem)
# mod_constant is the key, it's equal to every "test divisible number" of every monkey multiplied together

# An example of why this works (this is not pseudo-code, it's math):
# n % 2 = 1
# n % 5 = 3
# n % 7 = 5
# (Note how every divider is a prime number,
# same as all of the test divisible numbers of the monkeys)

# This would be the "mod_constant" equivalent:
# 2 * 5 * 7 = 70

# Now here's the magic, if you get the remainder of n and mod_constant:
# n % 70 = 33

# You STILL get the same remainders 
# when doing the modulus operations that we did at the start:
# 33 % 2 = 1
# 33 % 5 = 3
# 33 % 7 = 5

# That means that for this puzzle, instead of using the raw "n", which could become a really large number,
# we can instead get the remainder with mod_constant, so that we cap "n" to be smaller than mod_constant,
# because the modulus operations we do with the test divisible numbers will give the same results as if we didn't cap "n"

class Monkey():

    def __init__(self, items, operation, testDivisible, trueMonkey, falseMonkey):
        self.items = items
        self.operation = operation
        self.testDivisible = testDivisible
        self.trueMonkey = trueMonkey
        self.falseMonkey = falseMonkey
        self.inspectedItems = 0
    
    def ExecuteRoundActions(self):
        for index, item in enumerate(self.items):
            self.inspectedItems += 1;
            old = item
            self.items[index] = int(eval(self.operation) % mod_constant) 

            if self.items[index] % self.testDivisible:
                monkeys[self.trueMonkey].items.append(self.items[index])
            else:
                monkeys[self.falseMonkey].items.append(self.items[index])
        
        self.items = []


monkeys = []

# Parsing
for monkeyIndex in range(int((len(allLines) + 1) / 7)):
    itemsList = allLines[monkeyIndex * 7 + 1].removeprefix("  Starting items: ").removesuffix("\n")
    if itemsList != "": ims = list(map(int, itemsList.split(", ")))
    else: ims = []
    op = allLines[monkeyIndex * 7 + 2].removeprefix("  Operation: new = ").removesuffix("\n")
    testDiv = int(allLines[monkeyIndex * 7 + 3].removeprefix("  Test: divisible by "))
    fMonkey = int(allLines[monkeyIndex * 7 + 4].removeprefix("    If true: throw to monkey ").removesuffix("\n"))
    tMonkey = int(allLines[monkeyIndex * 7 + 5].removeprefix("    If false: throw to monkey ").removesuffix("\n"))

    monkey = Monkey(ims, op, testDiv, tMonkey, fMonkey)
    monkeys.append(monkey)

for round in range(10000):
    for monkey in monkeys:
        monkey.ExecuteRoundActions()

for monkey in monkeys:
    print(monkey.items)
    print(monkey.inspectedItems)

sortedInspectedItems = sorted([monkey.inspectedItems for monkey in monkeys])
print(sortedInspectedItems)
print(sortedInspectedItems[-1] * sortedInspectedItems[-2])