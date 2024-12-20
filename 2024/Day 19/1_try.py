from sys import stdin

towels = input().split(", ")
input()


def can_be_formed(pattern) -> bool:

    if len(pattern) == 0:
        return True

    can = False
    for towel in towels:
        if not towel in pattern:
            continue

        divided = pattern.split(towel)
        if all(can_be_formed(sub_patt) for sub_patt in divided):
            can = True

    return can


answer = 0
for line in stdin:
    pattern = line.strip()
    answer += int(can_be_formed(pattern))

print(answer)
