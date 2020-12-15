allYesSum = 0
numPeople = 0

currentSet = set(())
prevSet = set(())

with open("day6.txt", "r") as f:

    for line in f:

        line = line.strip("\n")

        if len(line) == 0:
            allYesSum += len(currentSet)
            currentSet = set(())
            prevSet = set(())
            numPeople = 0
        else:
            if numPeople == 0:
                currentSet = set(line)
            else:
                prevSet = currentSet.copy()
                currentSet = set(())
                for c in line:
                    if c in prevSet:
                        currentSet.add(c)
            numPeople += 1
                
allYesSum += len(currentSet)
print(allYesSum)