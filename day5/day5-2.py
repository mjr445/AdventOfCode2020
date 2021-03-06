import math

f = open("day5.txt", "r")

seatIDs = []
maxSeatID = 0

for line in f:

    upper_row = 127
    lower_row = 0

    upper_seat = 7
    lower_seat = 0

    for char in line:
        if char == "F":
            upper_row = math.floor( (upper_row + lower_row) / 2 )

        if char == "B":
            lower_row = math.floor( (upper_row + lower_row) / 2 )

        if char == "R":
            lower_seat = math.floor( (upper_seat + lower_seat) / 2 )

        if char == "L":
            upper_seat = math.floor( (upper_seat + lower_seat) / 2 )
    newSeatID = upper_row * 8 + upper_seat
    maxSeatID = max([maxSeatID, newSeatID])
    seatIDs.append(newSeatID)
    
f.close()

seatSet = set(seatIDs)

for ID in seatIDs:
    if ID+1 not in seatSet and ID+1 <= maxSeatID:
        print(ID+1)