from math import inf

with open("day13.txt", "r") as f:
    target = int(f.readline())
    nums = [int(val) for val in f.readline().strip().split(",") if val != "x"]

soonest = inf
soonest_idx = 0
for idx, num in enumerate(nums):
    diff = target - (target % num) + num - target
    if diff < soonest:
        soonest = diff
        soonest_idx = idx

print(nums[soonest_idx] * soonest)

