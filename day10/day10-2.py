oneJolt = 0
last_idx = 0
permutations = 1

with open("day10.txt", "r") as f:
    joltList = [0]
    for x in f.readlines():
        joltList.append(int(x))
    joltList.sort()
    joltList.append(joltList[-1]+3)

idx = 1
for adapter in joltList[:-1]:
    if joltList[idx] - adapter == 3:

        rangeSize = (idx - 2) - last_idx # Amount of numbers between
                                            # indices that have to stay

        # Ex.: [5, 6, 7, 8, 9], permuatations is 7
        # [5, 6, 7, 8, 9], [5, 6, 9], [5, 6, 7, 9], [5, 6, 8, 9], [5, 7, 9]
        # [5, 8, 9], [5, 7, 8, 9]
        if rangeSize == 3:
            permutations *= 7

        # Ex.: [11, 12, 13, 14], permutations is 4
        # [11, 14], [11, 12, 13, 14], [11, 12, 14], [11, 13, 14]
        elif rangeSize == 2: 
            permutations *= 4
        
        # Ex.: [23, 24, 25], permutations is 2
        # [23, 24, 25], [23, 25]
        elif rangeSize == 1:
            permutations *= 2
        last_idx = idx
    idx += 1

print(permutations)