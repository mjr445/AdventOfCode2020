f = open("day2.txt", "r")

validPasswords = 0
for line in f:
    
    bounds, letter, password = line.split()
    
    idx1, idx2 = bounds.split("-")
    idx1 = int(idx1) - 1
    idx2 = int(idx2) - 1

    char = letter.split(":")[0]

    password = password.lower()
    goalChar = char.lower()

    if (password[idx1] == char and password[idx2] != char) or \
        (password[idx2] == char and password[idx1] != char):
        validPasswords += 1
    else:
        continue
f.close()
print(validPasswords)