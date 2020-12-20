import re
x = 0
y = 0

dirs = ['E', 'S', 'W', 'N']
currentDir = 0

def moveShip(direction, value, x, y):
    if direction == 'N':
        y += value
    elif direction == 'S':
        y -= value
    elif direction == 'E':
        x += value
    elif direction == 'W':
        x -= value
    
    return x, y

with open("day12.txt", "r") as f:
    for line in f:
        action, value = re.split(r'(\d+)', line.strip())[:-1]
        if action == 'R':
            change = currentDir + int(value) / 90
            currentDir = int(change) if change < 4 else int(change - 4)
            continue
        
        if action == 'L':
            change = currentDir - int(value) / 90
            currentDir = int(change) if change >= 0 else int(change + 4)
            continue

        if action == 'F':
            x, y = moveShip(dirs[currentDir], int(value), x, y)
        else:
            x, y = moveShip(action, int(value), x, y)
        
dist = abs(x) + abs(y)
print(dist)