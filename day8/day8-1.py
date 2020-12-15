acc = 0

commands = []
executed = []
nextCommand = 0
i = 0
loop = False

with open("day8.txt", "r") as f:
    for line in f:

        command, value = line.split()
        commands.append([command, int(value)])
        executed.append(0)

        while i >= nextCommand:

            if executed[nextCommand] == 1:
                loop = True
                break

            command, value = commands[nextCommand]
            executed[nextCommand] = 1

            if command == "nop":
                nextCommand += 1
            elif command == "acc":
                acc += value
                nextCommand += 1
            elif command == "jmp":
                nextCommand += value
            

        i+=1
        if loop:
            break

print(acc)