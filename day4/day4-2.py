def isValid(field, value):

    if field == "byr":
        year = int(value)
        return (year >= 1920 and year <= 2002)

    if field == "iyr":
        year = int(value)
        return (year >= 2010 and year <= 2020)

    if field == "eyr":
        year = int(value)
        return (year >= 2020 and year <= 2030)

    if field == "hgt":
        if value[-2:] == "in":
            height = int(value[:-2])
            return (height >= 59 and height <= 76)
        elif value[-2:] == "cm":
            height = int(value[:-2])
            return (height >= 150 and height <= 193)
        else:
            return False

    if field == "hcl":
        if value[0] == "#":
            color = value[1:]
            for char in color:
                if (ord(char) >= 48 and ord(char) <= 57) or (ord(char) >= 97 and ord(char) <= 102):
                    pass
                else:
                    return False
            
            return True
        else:
            return False

    if field == "ecl":
        return (value in eyeColors)

    if field == "pid":
        return (len(value) == 9 and value.isnumeric())

f = open("day4.txt", "r")

validPassports = 0
fullSet = {"byr", "iyr", "eyr", "hgt",
            "hcl", "ecl", "pid", "cid"}

tempSet = fullSet.copy()

eyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

for line in f:

    line = line.strip("\n")

    if len(line) == 0:
        if (len(tempSet) == 0) or (len(tempSet) == 1 and "cid" in tempSet):
            validPassports += 1

        tempSet = fullSet.copy()
        continue

    line = line.split()
    for data in line:
        field, value = data.split(":")
        if isValid(field, value):
            tempSet.remove(field)

if (len(tempSet) == 0) or (len(tempSet) == 1 and "cid" in tempSet):
    validPassports += 1

f.close()
print(validPassports)
