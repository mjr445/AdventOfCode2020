from collections import OrderedDict

queueSet = OrderedDict()
valid = False

with open("day9.txt", "r") as f:
    for x in range(25):
        queueSet[int(next(f))] = None
    
    for line in f: # Length of (file - 25) at worst
        num = int(line)
        for key in queueSet: # 25 iterations at worst
            if num - key in queueSet: # O(1)
                valid = True
                break
        if not valid:
            print(num)
            break
        valid = False
        queueSet.popitem(last=False) # O(1)
        queueSet[num] = None # O(1)
