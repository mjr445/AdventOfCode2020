acc = 0

commands = []
executed = []
nextCommand = 0
i = 0
changed = False
oldState = {}

with open("day8.txt", "r") as f:
    for line in f:

        command, value = line.split()
        commands.append([command, int(value)])
        executed.append(0)

        while i >= nextCommand:

            if commands[nextCommand][0] == "jmp" and not changed:
                # print(nextCommand)
                commands[nextCommand][0] = "nop"
                oldState['acc'] = acc
                oldState['nextCommand'] = nextCommand
                oldState['executed'] = executed
                changed = True
            
            elif commands[nextCommand][0] == "nop" and not changed:
                # print(nextCommand)
                commands[nextCommand][0] = "jmp"
                oldState['acc'] = acc
                oldState['nextCommand'] = nextCommand
                oldState['executed'] = executed
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

            if i >= nextCommand and executed[nextCommand] == 1: # Loop found
                print("Loop found switching: ", oldState['nextCommand'], "Command causing loop", nextCommand)

                
                acc = oldState['acc']
                nextCommand = oldState['nextCommand']
                executed = oldState['executed']
    
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
            

        i+=1

print(acc)