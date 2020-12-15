import re

numColors = 0
bagTree = {} # Use dictionary as tree

with open("day7.txt", "r") as f:

    for line in f:
        
        line = line.strip("\n")

        line = re.split("bags contain|bags, |bags.|bag, |bag.", line)

        mainBag = line[0].strip()
        if mainBag not in bagTree:

            bagTree[mainBag] = {}

        for bag in line[1:-1]:
            bag = bag.strip()
            if bag[0] == 'n':
                continue
            num, bag = bag.split(' ', 1)
            if bag not in bagTree[mainBag]:
                bagTree[mainBag][bag] = int(num)

totalBags = []

def dfs(graph, node, prevNode, multiplier):

    for neighbour in graph[node]:
        # print(graph[node][neighbour])
        leafTotal = graph[node][neighbour] * multiplier
        totalBags.append(leafTotal)
        if not graph[neighbour]: # Dictionary is empty (is a leaf)
            pass
        else:
            dfs(graph, neighbour, node, leafTotal)

dfs(bagTree, 'shiny gold', None, 1)

print(sum(totalBags))    
