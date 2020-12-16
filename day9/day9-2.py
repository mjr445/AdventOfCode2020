from collections import OrderedDict

queueSet = OrderedDict()
valid = False
breakPoint = -1

with open("day9.txt", "rb") as f:
    content = f.readlines()

for x in range(25):
    queueSet[int(content[x])] = None

idx = 25
for line in content[25:]: # Length of (file - 25) at worst
    num = int(line)
    for key in queueSet: # 25 iterations at worst
        if num - key in queueSet: # O(1)
            valid = True
            break
    if not valid:
        breakPoint = num
        break
    valid = False
    queueSet.popitem(last=False) # O(1)
    queueSet[num] = None # O(1)
    idx += 1

queueSet = OrderedDict(reversed(list(queueSet.items()))) # Reverse order
contiguousSum = sum(queueSet.keys())
idx -= 26

while contiguousSum != breakPoint:
    if contiguousSum > breakPoint:
        num, _ = queueSet.popitem(last=False)
        contiguousSum -= num
    elif contiguousSum < breakPoint:
        num = int(content[idx])
        contiguousSum+=num
        queueSet[num] = None
        idx-=1
    if idx < 0:
        print("Failed")
        break

bound1, _ =  min(queueSet.items(), key=lambda x: x[0]) 
bound2, _ = max(queueSet.items(), key=lambda x: x[0]) 
print(bound1 + bound2)
