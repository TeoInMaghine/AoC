import os
import math

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

instructions = allLines[0].strip()
instructions = [0 if i == 'L' else 1 for i in instructions]
instructions_count = len(instructions)
print(instructions)

nodes = {}
starting_nodes = set()
ending_nodes = set()

adsfasdf = 0

allLines = allLines[2:]
for line in allLines:
    sline = line.strip()
    node, neighbours = sline.split(" = ")
    neighbours = neighbours.removeprefix("(")
    neighbours = neighbours.removesuffix(")")
    neighbours = neighbours.split(", ")

    nodes[node] = neighbours

    if node.endswith("A"):
        adsfasdf += 1
        # I changed this line from 1 to 6 to get the numbers
        # in end_nodes.txt
        if(adsfasdf == 6):
            starting_nodes.add(node)
    elif node.endswith("Z"):
        ending_nodes.add(node)

print(nodes)

steps = 0
current_nodes_are_end = False
while not current_nodes_are_end:
    new_current_nodes = set()
    current_instruction = instructions[steps % instructions_count]

    for node in starting_nodes:
        new_current_nodes.add(nodes[node][current_instruction])

    starting_nodes = new_current_nodes
    steps += 1

    current_nodes_are_end = starting_nodes.issubset(ending_nodes)
    if current_nodes_are_end:
        print(starting_nodes)

print(steps)

print("Result")
print(math.lcm(12169, 20093, 20659, 22357, 13301, 18961))