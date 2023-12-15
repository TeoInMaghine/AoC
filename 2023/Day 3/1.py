import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

potential_gears_positions = []

number_index = 0
numbers = []
# pos: number_index
number_positions = {}

for row, line in enumerate(allLines):
    sline = line.strip()

    temp_num = ""
    for column, char in enumerate(sline):

        if char.isnumeric():
            temp_num += char
        elif temp_num != "":
            number = int(temp_num)
            width = len(temp_num)
            temp_num = ""
            numbers.append(number)

            for i in range(column - width, column):
                number_positions[(row, i)] = number_index

            number_index += 1
            if char == "*":
                potential_gears_positions.append((row, column))
        elif char == "*":
            potential_gears_positions.append((row, column))

result = 0

for spos in potential_gears_positions:
    temp_result = 1
    adjacent_nums_count = 0

    for row in range(spos[0]-1, spos[0]+2):
        for column in range(spos[1]-1, spos[1]+2):
            pos = (row, column)
            if pos in number_positions:
                index = number_positions[pos]
                if numbers[index] != None:
                    adjacent_nums_count += 1
                    temp_result *= numbers[index]
                    print(numbers[index])
                    numbers[index] = None
    
    if adjacent_nums_count == 2:
        result += temp_result

print(result)
