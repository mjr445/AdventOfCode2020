# Had to take a peek at the subreddit solutions, learned about Chinese Remainder Theorem

from collections import OrderedDict

# Source for CRT: Rosetta Code (https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6)
from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
# Rosetta Code CRT ends

busStops = OrderedDict()

with open("day13.txt", "r") as f:
    f.readline()
    nums = f.readline().strip().split(",")
n = []
a = []
for idx, num in enumerate(nums):
    if num != "x":
        num = int(num)
        if idx == 0:
            n.append(num)
            a.append(idx)
        else:
            n.append(num)
            new_a = num - idx
            while new_a < 0:
                new_a += num
            a.append(new_a)

solution = chinese_remainder(n, a)
print(solution)
