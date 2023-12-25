import os

allLines = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'input.txt')) as f:
    allLines = f.readlines()

steps = allLines[0].split(',')

boxes = {}
for step in steps:

    focal_length = None
    if step.find('=') != -1:
        label, focal_length = step.split('=')
        focal_length = int(focal_length)
    elif step[-1] == '-':
        label = step[:-1]

    box_index = 0
    for char in label:
        ascii = ord(char)
        box_index += ascii
        box_index *= 17
        box_index %= 256
    
    # Case with '-' (dash) character
    # Remove lenses with given label
    if focal_length == None and box_index in boxes:
        box = boxes[box_index]
        boxes[box_index] = [lens for lens in box if lens[0] != label]
    # Case with '=' character
    else:
        if box_index not in boxes:
            boxes[box_index] = []
            boxes[box_index].append((label, focal_length))
        else:
            found_label = False
            for lens_index, lens in enumerate(boxes[box_index]):
                if lens[0] == label:
                    found_label = True
                    boxes[box_index][lens_index] = label, focal_length
            
            if not found_label:
                boxes[box_index].append((label, focal_length))

# print(boxes)

result = 0
for box_index, box in boxes.items():
    for lens_index, lens in enumerate(box):
        result += (box_index + 1) * (lens_index + 1) * lens[1]

print(result)