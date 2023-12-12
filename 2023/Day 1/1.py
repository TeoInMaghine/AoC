import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

string_numbers = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
result = 0
for line in allLines:

    sLine = line.strip()
    nums = []
    string = ""

    for char in sLine:
        if char.isnumeric():
            nums.append(int(char))
            string = ""
        else:
            string += char
            if len(string) >= 3:
                for key in string_numbers.keys():
                    if string.endswith(key):
                        nums.append(string_numbers[key])

    print(nums)
    result += 10 * nums[0] + nums[-1]

print(result)