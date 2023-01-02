# https://adventofcode.com/2022/day/12

List = open("E:\\Temp\\input12.txt")

Nodes = []
S = ['a', -1, []]
E = ['z', 0, []]

for row in List:
    Nodes.append([])
    for n in row:
        if n == 'S':
            Nodes[-1].append(S)
        elif n == 'E':
            Nodes[-1].append(E)
        else:
            Nodes[-1].append([n, -1, []])

def addValidNode(cNode, aNode):
    if ord(cNode[0]) - ord(aNode[0]) <= 1:
        cNode[2].append(aNode)

for r in range(len(Nodes)):
    for c in range(len(Nodes[r])):
        if r > 0:               addValidNode(Nodes[r][c], Nodes[r-1][c])
        if r < len(Nodes)-1:    addValidNode(Nodes[r][c], Nodes[r+1][c])
        if c > 0:               addValidNode(Nodes[r][c], Nodes[r][c-1])
        if c < len(Nodes[r])-1: addValidNode(Nodes[r][c], Nodes[r][c+1])

Q = [E]
while Q:
    node = Q.pop(0)
    for p in node[2]:
        if p[1] == -1:
            p[1] = node[1]+1
            Q.append(p)

print(S[1])

print(min(n[1] for r in Nodes for n in r if n[0] == 'a' and n[1] != -1))
