f = open("day3.txt", "r")

col = 0
numTrees = 0

line = f.readline()
blockLen = len(line.strip())

for line in f: 

    col+=3

    if col >= blockLen:
        col = col - blockLen
    if line[col] == "#":
        numTrees += 1

f.close()
print(numTrees)