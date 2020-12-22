import re
valid = set()

with open("day16.txt", "r") as f:
    line = f.readline().strip()
    while line != "":
        line = re.split(": | or |-", line)
        line = [int(x) for x in line[1:]]

        # Add all valid numbers to a set
        for n in range(line[0], line[1]+1):
            valid.add(n)
        for n in range(line[2], line[3]+1):
            valid.add(n)
        
        line = f.readline().strip()
    
    line = f.readline().strip()
    while line != "":
        line = f.readline().strip()
    line = f.readline().strip()
    sum = 0
    for line in f:
        line = [int(x) for x in line.strip().split(",")]
        for n in line:
            if n not in valid:
                sum += n

print(sum)