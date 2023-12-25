import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

patterns = [[]]
for line in allLines:
    sline = line.strip()

    if sline == "":
        patterns.append([])
        continue
    
    patternIndex = len(patterns) - 1

    patterns[patternIndex].append(sline)

def get_smudges(pattern, i, possible_mirror_count):
    # Comparisons to be made, minimum between distance to left and right
    comparisons_to_be_done = min(i + 1, possible_mirror_count - i)

    smudges = 0
    for j in range(comparisons_to_be_done):
        # Make character to character comparison to notice smudges
        for left_char, right_char in zip(pattern[i-j], pattern[i+j+1]):
            print(left_char, right_char)
            if left_char != right_char:
                smudges += 1
            if smudges > 1:
                return smudges
    
    return smudges

def get_elements_before_mirror(pattern):
    # print(pattern)
    possible_mirror_count = len(pattern) - 1
    for i in range(possible_mirror_count):

        smudges = get_smudges(pattern, i, possible_mirror_count)
        print(smudges)

        if smudges == 1:
            return i + 1
    
    return 0

result = 0

for pattern in patterns:

    print(f"Row-based pattern: {get_elements_before_mirror(pattern)}")
    result += 100 * get_elements_before_mirror(pattern)

    # Switch rows for columns
    first_row = pattern[0]
    column_pattern = ["" for column in first_row]

    for row in pattern:
        for column, char in enumerate(row):
            column_pattern[column] += char

    print(f"Column-based pattern: {get_elements_before_mirror(column_pattern)}")
    result += get_elements_before_mirror(column_pattern)

print(result)