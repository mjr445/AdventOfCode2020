with open("day15.txt", "r") as f:
    nums = [int(x) for x in f.readline().strip().split(",")]

spoken = {}

for turn in range(len(nums)):
    spoken[nums[turn]] = [turn+1, None]

new = True
lastSpoken = -1
for turn in range(len(nums) + 1, 2021):
    if new:
        spoken[0][1] = spoken[0][0]
        spoken[0][0] = turn
        lastSpoken = 0
        new = False
    else:
        lastSpoken = spoken[lastSpoken][0] - spoken[lastSpoken][1]
        if lastSpoken in spoken:
            new = False
            spoken[lastSpoken][1] = spoken[lastSpoken][0]
            spoken[lastSpoken][0] = turn
        else:
            new = True
            spoken[lastSpoken] = [turn, None]

print(lastSpoken)
