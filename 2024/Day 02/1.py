import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()


reports = [list(map(int, line.split())) for line in allLines]

def safe(report):
    ascending = report[0] < report[1]

    for prev_level, level in zip(report[:-1], report[1:]):
        asc_diff = level - prev_level
        desc_diff = -asc_diff

        if ascending:
            if 1 <= asc_diff <= 3:
                continue
        else:
            if 1 <= desc_diff <= 3:
                continue

        return False

    return True

safe_reports = 0
for report in reports:
    if safe(report):
        print(report)
        safe_reports += 1

print(safe_reports)

