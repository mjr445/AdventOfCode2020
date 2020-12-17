oneJolt = 0
threeJolt = 0

with open("day10.txt", "r") as f:
    joltList = [int(x) for x in f.readlines()]
    joltList.sort()

idx = 1
for adapter in joltList[:-1]:
    if joltList[idx] - adapter == 1:
        oneJolt += 1
    elif joltList[idx] - adapter == 3:
        threeJolt += 1
    idx += 1

threeJolt += 1 # To connect to your device

if joltList[0] == 1: # Outlet to first adapter is 1
    oneJolt += 1 
elif joltList[0] == 3: # Outlet to first adapter is 3
    threeJolt += 1

print(oneJolt * threeJolt)