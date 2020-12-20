import re
x, way_x, y, way_y = 0, 10, 0, 1

dirs = ['E', 'S', 'W', 'N']

currentDir = 0

def rotateWaypoint(action, value, dirs, currentDir, way_x, way_y):

    oldDir = currentDir

    if action == 'R':
        change = currentDir + int(value) / 90
        currentDir = int(change) if change < 4 else int(change - 4)
        
    elif action == 'L':
        change = currentDir - int(value) / 90
        currentDir = int(change) if change >= 0 else int(change + 4)
    
    if dirs[oldDir] in ['E', 'W'] and dirs[currentDir] in ['S', 'N']:
        if dirs[currentDir] == 'N':
            new_way_y = abs(way_x)
        else:
            new_way_y = -1*(abs(way_x))

        secondaryDir = currentDir - 1 if currentDir - 1 >= 0 else currentDir - 1 + 4
        if dirs[secondaryDir] == 'E':
            new_way_x = abs(way_y)
        else:
            new_way_x = -1*abs(way_y)
    
    elif dirs[oldDir] in ['S', 'N'] and dirs[currentDir] in ['E', 'W']:
        if dirs[currentDir] == 'E':
            new_way_x = abs(way_y)
        else:
            new_way_x = -(abs(way_y))
        secondaryDir = currentDir - 1 if currentDir - 1 >= 0 else currentDir - 1 + 4
        if dirs[secondaryDir] == 'N':
            new_way_y = abs(way_x)
        else:
            new_way_y = -1*abs(way_x)
    
    else:
        new_way_x = -1*way_x
        new_way_y = -1*way_y

    return new_way_x, new_way_y, currentDir


def moveWaypoint(direction, value, way_x, way_y):
    if direction == 'N':
        way_y += value
    elif direction == 'S':
        way_y -= value
    elif direction == 'E':
        way_x += value
    elif direction == 'W':
        way_x -= value
    
    return way_x, way_y

with open("day12.txt", "r") as f:
    for line in f:
        action, value = re.split(r'(\d+)', line.strip())[:-1]
        if action in ['R', 'L']:
            way_x, way_y, currentDir = rotateWaypoint(action, value, dirs, currentDir, way_x, way_y)

        elif action == 'F':
            x += int(value) * way_x
            y += int(value) * way_y
        
        else:
            way_x, way_y = moveWaypoint(action, int(value), way_x, way_y)

dist = abs(x) + abs(y)
print(dist)