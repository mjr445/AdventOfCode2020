import numpy as np

f = open("day3.txt", "r")

# 11, 31, 51, 71, 12
cols = [0, 0, 0, 0, 0]

numTrees = [0, 0, 0, 0, 0]

line = f.readline()
blockLen = len(line.strip())

read12 = False

for line in f: 

    cols[0] += 1
    cols[1] += 3
    cols[2] += 5
    cols[3] += 7
    if read12:
        cols[4] += 1


    for idx, col in enumerate(cols):
        if col >= blockLen:
            cols[idx] -= blockLen
            col = cols[idx]

        if idx==4 and not read12:
            continue
        
        if line[col] == "#":
            numTrees[idx] += 1
    
    read12 = not read12

f.close()
print(np.prod(numTrees))