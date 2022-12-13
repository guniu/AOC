# https://adventofcode.com/2022/day/12

List = open("E:\\Temp\\input12.txt").read().splitlines()

Nodes = []
S = None
E = None
Q = []

for row in List:
    Nodes.append([])
    for n in row:
        if n == 'S':
            S = ['a', -1, []]
            Nodes[-1].append(S)
        elif n == 'E':
            E = ['z', 0, []]
            Nodes[-1].append(E)
        else:
            Nodes[-1].append([n, -1, []])
    Q.extend(Nodes[-1])

def addValidNode(cNode, aNode):
    if ord(cNode[0]) - ord(aNode[0]) <= 1:
        cNode[2].append(aNode)

for r in range(len(Nodes)):
    for c in range(len(Nodes[r])):
        if r > 0:               addValidNode(Nodes[r][c], Nodes[r-1][c])
        if r < len(Nodes)-1:    addValidNode(Nodes[r][c], Nodes[r+1][c])
        if c > 0:               addValidNode(Nodes[r][c], Nodes[r][c-1])
        if c < len(Nodes[r])-1: addValidNode(Nodes[r][c], Nodes[r][c+1])

def extractClosestNode():
    smallest = -1
    index    = -1
    for i in range(len(Q)):
        if Q[i][1] != -1:
            if smallest == -1 or Q[i][1] < smallest:
                smallest = Q[i][1]
                index = i
    return Q.pop(index)

while Q:  # S[1] == -1:
    node = extractClosestNode()
    if node[1] == -1: break
    for p in node[2]:
        # if p in Q:  # "recursion depth exceeded in comparison"
        if p[1] == -1:  # or node[1]+1 < p[1]:
            p[1] = node[1]+1

print(S[1])

print(min(n[1] for r in Nodes for n in r if n[0] == 'a' and n[1] != -1))
