import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

histories = [[int(num) for num in line.strip().split()[::-1]]for line in allLines]

def get_diffs(sequence):
    all_zeroes = True
    diff_seq = []

    for left, right in zip(sequence, sequence[1:]):
        diff = right - left
        diff_seq.append(diff)

        if diff != 0: all_zeroes = False
    
    # print(diff_seq)
    return diff_seq, all_zeroes

def predict_next(sequence):

    diff_seq, all_zeroes = get_diffs(sequence)
    if all_zeroes:
        return sequence[-1]
    else:
        return sequence[-1] + predict_next(diff_seq)

result = 0
for history in histories:
    result += predict_next(history)

print(result)