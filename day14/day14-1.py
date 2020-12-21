import re
mem = {}
with open("day14.txt", "r") as f:
    for line in f:
        action, value = line.split("=")
        action = action.strip()
        value = value.strip()
        if action == 'mask':
            toChange = []
            mask = list(value)
            for idx, char in enumerate(value):
                if char == "X":
                    toChange.append(35 - idx)
        else:
            maskCopy = mask.copy()
            for idx in range(len(toChange) - 1, -1, -1):
                value = int(value)
                bitStatus = (value >> toChange[idx]) & 1
                maskCopy[35 - toChange[idx]] = str(bitStatus)
            bitString = ''
            for bit in maskCopy:
                bitString += bit
            finalVal = int(bitString, 2)
            memSpot = int(re.search(r"\[([0-9_]+)\]", action).group(1))
            mem[memSpot] = finalVal

sum = 0
for val in mem.values():
    sum += val
print(sum)