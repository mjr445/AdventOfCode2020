import re
import numpy as np

validNums = set()
bounds = []
combos = np.ones((20,20))
possibleColumns = [20] * 20

with open("day16.txt", "r") as f:
    line = f.readline().strip()
    while line != "":
        line = re.split(": | or |-", line)
        line = [int(x) for x in line[1:]]

        bounds.append(line)
        # Add all valid numbers to a set
        for n in range(line[0], line[1]+1):
            validNums.add(n)
        for n in range(line[2], line[3]+1):
            validNums.add(n)
        
        line = f.readline().strip()
    
    f.readline()
    myTicket = [int(x) for x in f.readline().strip().split(",")]
    for i, n in enumerate(myTicket):
        for j, bound in enumerate(bounds):
            if not (bound[0]<=n<=bound[1] or bound[2]<=n<=bound[3]):
                combos[i][j] = 0
    
    f.readline()
    f.readline()
    for line in f:
        isValid = True
        line = [int(x) for x in line.strip().split(",")]
        for n in line:
            if n not in validNums and isValid:
                isValid = False
        if isValid:
            for i, n in enumerate(line):
                for j, bound in enumerate(bounds):
                    if not (bound[0]<=n<=bound[1] or bound[2]<=n<=bound[3]):
                        combos[i][j] = 0
    
    checked = set(())
    field = 0
    colsLeft = 20
    while colsLeft > 0:
        numOnes = np.count_nonzero(combos[field] == 1)
        if numOnes == 1 and field not in checked:
            col = np.where(combos[field] == 1)
            for i in range(0, 20):
                if i == field:
                    pass
                else:
                    combos[i][col] = 0
            checked.add(field)
            field = 0
            colsLeft -= 1
        else:
            field += 1
finalProd = 1
combos = np.transpose(combos)
for i in range(0, 6):
    col = np.where(combos[i] == 1)
    finalProd *= myTicket[col[0][0]]
print(finalProd)