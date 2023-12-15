import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

cards = []
for line in allLines:
    sline = line.strip()
    # replace two spaces with one for easier parsing
    sline = sline.replace("  ", " ")

    _, all_nums = sline.split(": ")
    your_nums, winning_nums = all_nums.split(" | ")
    
    your_nums = your_nums.split(" ")
    winning_nums = winning_nums.split(" ")
    
    your_nums = [int(e) for e in your_nums]
    winning_nums = {int(e) for e in winning_nums}

    cards.append((your_nums, winning_nums))

memo = {}
cards_count = 0

def get_cards(card_index):
    if card_index in memo:
        return memo[card_index]

    your_nums, winning_nums = cards[card_index]
    generated_cards = 1

    won_cards = 0
    for num in your_nums:
        if num in winning_nums:
            won_cards += 1
            generated_cards += get_cards(card_index + won_cards)
    
    memo[card_index] = generated_cards
    return generated_cards

for card_index, card in enumerate(cards):
    cards_count += get_cards(card_index)

print(cards_count)
