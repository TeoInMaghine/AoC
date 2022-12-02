with open('input.txt', 'r') as file:
    allLines = file.read().splitlines()

t = ""
for char in allLines[0]:
    t += f"{int(char, 16):04b}"

def LiteralValue(text):
    number = ""
    i = 1
    while True:
        number += text[i:i+4]
        prefix = int(text[i-1], 2)
        if prefix == 0:            
            return int(number, 2), i+4
        i += 5

def Unpack(text, spLength, spCount):
    global versionNumSum

    print(f"\nspLength: {spLength} - spCount: {spCount}")
    print(f"text: {text}")
    version = int(text[0:3], 2)
    typeID = int(text[3:6], 2)
    nCharacters = 6
    print(f"version: {version} - type ID: {typeID}")
    versionNumSum += version

    if typeID == 4:        
        value, nChars = LiteralValue(text[6:])
        nCharacters += nChars
        print(f"value: {value} - nCharacters: {nCharacters}")
    else:
        lengthTypeID = int(text[6], 2)
        print(f"lengthTypeID: {lengthTypeID}")
        if lengthTypeID == 0:
            nCharacters += 16
            
            length = int(text[7:(7+15)], 2)
            nCharacters += length
            subpackets = text[(7+15):]
            print(f"subpackets: {subpackets} - length: {length}")
            while length > 0:     
                nChrs, subpackets, length = Unpack(subpackets, length, None)
        else:
            nCharacters += 12

            count = int(text[7:(7+11)], 2)
            subpackets = text[(7+11):]            
            print(f"subpackets: {subpackets} - count: {count}")
            while count > 0:
                nChrs, subpackets, count = Unpack(subpackets, None, count)
                nCharacters += nChrs
            print(f"text: {text} NCHARACTERS!!!!: {nCharacters}")
    
    if spLength is not None:
        return nCharacters, text[nCharacters:], spLength - nCharacters
    elif spCount is not None:
        return nCharacters, text[nCharacters:], spCount - 1

versionNumSum = 0
Unpack(t, None, None)
print(versionNumSum)