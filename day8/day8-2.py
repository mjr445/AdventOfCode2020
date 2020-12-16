acc = 0

commands = []
executed = []
nextCommand = 0
changed = False
oldState = {}

with open("day8.txt", "r") as f:
    for line in f:

        command, value = line.split()
        commands.append([command, int(value)])
        executed.append(0)

while len(executed) > nextCommand:

    if commands[nextCommand][0] == "jmp" and not changed:
        commands[nextCommand][0] = "nop"
        oldState['acc'] = acc
        oldState['nextCommand'] = nextCommand
        oldState['executed'] = executed.copy()
        changed = True
    
    elif commands[nextCommand][0] == "nop" and not changed:
        commands[nextCommand][0] = "jmp"
        oldState['acc'] = acc
        oldState['nextCommand'] = nextCommand
        oldState['executed'] = executed.copy()
        changed = True
    
    command, value = commands[nextCommand]
    executed[nextCommand] = 1

    if command == "nop":
        nextCommand += 1
    elif command == "acc":
        acc += value
        nextCommand += 1
    elif command == "jmp":
        nextCommand += value
    
    
    if nextCommand < len(executed) and executed[nextCommand] == 1: # Loop found
        acc = oldState['acc']
        nextCommand = oldState['nextCommand']
        executed = oldState['executed'].copy()

        changed = False
        commands[nextCommand][0] = "jmp" if commands[nextCommand][0] == "nop" else "nop"
        command, value = commands[nextCommand]
        executed[nextCommand] = 1

        if command == "nop":
            nextCommand += 1
        elif command == "acc":
            acc += value
            nextCommand += 1
        elif command == "jmp":
            nextCommand += value

print(acc)