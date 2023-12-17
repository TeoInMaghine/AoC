import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

def get_hand_type(hand):
    jokers = 0
    kinds = {}
    for card in hand:
        if card == 'J':
            jokers += 1
        elif card in kinds:
            kinds[card] += 1
        else: kinds[card] = 1
    
    values = sorted(kinds.values(), reverse=True)
    if len(values) == 0: values.append(0)
    values[0] += jokers
    kinds_count = len(values)

    if   kinds_count == 1:
        return 6
    elif kinds_count == 2:
        if values[0] == 4:
            return 5
        else:
            return 4
    elif kinds_count == 3:
        if values[0] == 3:
            return 3
        if values[0] == 2 and values[1] == 2:
            return 2
    elif kinds_count == 4:
        if values[0] == 2:
            return 1
    
    return 0

value_table = "J23456789TJQKA"
def get_value(hand):
    value = 0
    base_14_digit_mult = 1

    hand = hand[::-1]
    for card in hand:
        value += base_14_digit_mult * value_table.find(card)
        base_14_digit_mult *= 14

    return value

most_significant_digit_mult = pow(14, 5)
values_to_bid = {}

for line in allLines:
    sline = line.strip()

    hand, bid = sline.split()
    bid = int(bid)

    # Define type
    type_value = get_hand_type(hand)

    # Diff inside same type
    hand_value = get_value(hand)

    value = most_significant_digit_mult * type_value + hand_value
    values_to_bid[value] = bid

    print(hand, value, bid)

# Sort values to determine rank
values_to_bid = dict(sorted(values_to_bid.items()))
print(values_to_bid)

result = 0
rank = 1
for value, bid in values_to_bid.items():
    result += rank * bid

    rank += 1

print(result)