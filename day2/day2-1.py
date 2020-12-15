f = open("day2.txt", "r")

validPasswords = 0
for line in f:
    
    bounds, letter, password = line.split()
    
    min, max = bounds.split("-")
    min = int(min)
    max = int(max)

    char = letter.split(":")[0]
    charCount = 0

    password = password.lower()
    goalChar = char.lower()

    for letter in password:
        if letter == goalChar:
            charCount += 1
    
    if charCount < min or charCount > max:
        continue
    else:
        validPasswords += 1
f.close()
print(validPasswords)
