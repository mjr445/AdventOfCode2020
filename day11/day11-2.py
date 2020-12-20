import copy

points = [(1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)]

with open("day11.txt", "r") as f:
    prevChart = [list(line.strip().replace("L", "#")) for line in f.readlines()]


def changeSeat(prevChart, coord, rows, cols):
    points = [(1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)]
    x_ref, y_ref = coord
    if prevChart[x_ref][y_ref] == ".":
        return False
    
    numOccupied = 0

    for x, y in points:
        i = 1
        while 0 <= x_ref + i * x < rows and 0 <= y_ref + i * y < cols:
            if prevChart[x_ref + i * x][y_ref+i*y] == "#":
                numOccupied += 1
                break
            if prevChart[x_ref + i * x][y_ref+i*y] == "L":
                break
            i += 1

    if prevChart[x_ref][y_ref] == "L" and numOccupied == 0:
        return True
    if prevChart[x_ref][y_ref] == "#" and numOccupied >= 5:
        return True
    
    return False
    
rows = len(prevChart)
cols = len(prevChart[0])
currentChart = copy.deepcopy(prevChart)
numTaken = 0
changed = True

while changed:
    changed = False
    prevChart = copy.deepcopy(currentChart)
    numTaken = 0

    for row in range(0, rows):
        for col in range(0, cols):
            if changeSeat(prevChart, (row, col), rows, cols):
                changed = True
                if prevChart[row][col] == "L":
                    currentChart[row][col] = "#"
                    numTaken += 1
                elif prevChart[row][col] == "#":
                    currentChart[row][col] = "L"
            else:
                if prevChart[row][col] == "#":
                    numTaken += 1
print(numTaken)