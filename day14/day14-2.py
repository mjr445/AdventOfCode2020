import re

mem = {}

def changeBit(memIdx, xLoc, mem, value):
    idx = xLoc[0]
    if len(xLoc) == 1:
        mem[memIdx] = value
        memIdx ^= (1 << idx)
        mem[memIdx] = value
    else:
        xLoc = xLoc[1:]
        changeBit(memIdx, xLoc, mem, value)
        memIdx ^= (1 << idx)
        changeBit(memIdx, xLoc, mem, value)


with open("day14.txt", "r") as f:
    for line in f:
        action, value = line.split("=")
        action = action.strip()
        if action == 'mask':
            value = value.strip()
            xLoc = []
            oneLoc = []
            for idx, char in enumerate(value):
                if char == "X":
                    xLoc.append(35 - idx)
                elif char == "1":
                    oneLoc.append(35 - idx)
        else:
            value = int(value)
            memIdx = int(re.search(r"\[([0-9_]+)\]", action).group(1))
            for idx in oneLoc:
                memIdx = (1 << idx) | memIdx

            changeBit(memIdx, xLoc, mem, value)

sum = 0
for val in mem.values():
    sum += val
print(sum)