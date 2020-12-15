yesSum = 0

with open("day6.txt", "r") as f:

    yesSet = set(())
    for line in f:

        line = line.strip("\n")

        if len(line) == 0:
            yesSum += len(yesSet)
            yesSet = set(())
        else:
            for char in line:
                yesSet.add(char)
yesSum += len(yesSet)
print(yesSum)