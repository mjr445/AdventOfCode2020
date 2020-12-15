f = open("day4.txt", "r")

validPassports = 0
fullSet = {"byr", "iyr", "eyr", "hgt",
            "hcl", "ecl", "pid", "cid"}

tempSet = fullSet.copy()

for line in f:

    line = line.strip("\n")

    if len(line) == 0:
        if (len(tempSet) == 0) or (len(tempSet) == 1 and "cid" in tempSet):
            validPassports += 1

        tempSet = fullSet.copy()

        continue

    line = line.split()
    for data in line:
        field, _ = data.split(":")
        tempSet.remove(field)

if (len(tempSet) == 0) or (len(tempSet) == 1 and "cid" in tempSet):
    validPassports += 1

f.close()
print(validPassports)