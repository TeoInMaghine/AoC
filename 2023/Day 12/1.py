import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

# Parsing
rows = []
for line in allLines:
    sline = line.strip()
    conditions, groups = sline.split()

    groups = [int(group) for group in groups.split(",")]

    rows.append((conditions, groups))

def is_valid(conditions, groups):
    i = 0
    for group in groups:
        current_contigous = 0
        
        while i < len(conditions):
            char = conditions[i]
            if char == '#':
                current_contigous += 1
            
            if current_contigous > group:
                return False
            
            if char == '.' and current_contigous > 0:
                if current_contigous != group:
                    return False
                
                current_contigous = 0
                break

            i += 1

            if i >= len(conditions) and current_contigous != group:
                return False
    
    return True

def determine_combinations(conditions, groups):
    i = 0
    for group in groups:
        first_unknown = conditions.find('?')

        if first_unknown == -1:
            return conditions
        
        

for row in rows:
    conditions, groups = row


    print(is_valid(conditions, groups))