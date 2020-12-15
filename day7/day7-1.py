import re

numColors = 0
bagTree = {} # Use dictionary as tree

with open("day7.txt", "r") as f:

    for line in f:
        
        line = line.strip("\n")

        line = re.split("bags contain|bags, |bags.|bag, |bag.", line)

        mainBag = line[0].strip()
        if mainBag not in bagTree:

            bagTree[mainBag] = set(())

        for bag in line[1:-1]:
            bag = bag.strip()
            if bag[0] == 'n':
                continue
            _, bag = bag.split(' ', 1)
            if bag not in bagTree[mainBag]:
                bagTree[mainBag].add(bag)

containsSGold = set(()) # Set to keep track of visited nodes.
visited = set(())

def dfs(visited, graph, node, currentPath):
    if node not in visited:
        currentPath.add(node)
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour in containsSGold:
                containsSGold.update(currentPath)
            elif neighbour == "shiny gold":
                containsSGold.update(currentPath)
            else:
                dfs(visited, graph, neighbour, currentPath.copy())

for bag in bagTree:
    dfs(visited, bagTree, bag, set(()))

print(len(containsSGold))