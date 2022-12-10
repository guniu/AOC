# https://adventofcode.com/2022/day/9

List = open("E:\\Temp\\input9.txt")

Rope = [[0, 0] for _ in range(10)]
Pos1 = {tuple(Rope[1])}
Pos2 = {tuple(Rope[-1])}

def updateTail(knot1, knot2):
    xDiff = knot1[0] - knot2[0]
    yDiff = knot1[1] - knot2[1]
    if abs(xDiff) > 1:
        knot2[0] += xDiff//abs(xDiff)
        if yDiff: knot2[1] += yDiff//abs(yDiff)
    elif abs(yDiff) > 1:
        knot2[1] += yDiff//abs(yDiff)
        knot2[0] = knot1[0]

def moveHead(coord, steps):
    for _ in range(abs(steps)):
        Rope[0][coord] += steps//abs(steps)
        for i in range(len(Rope)-1):
            updateTail(Rope[i], Rope[i+1])
        Pos1.add(tuple(Rope[1]))
        Pos2.add(tuple(Rope[-1]))

for line in List:
    line = line.split()
    if line[0] == "R":
        moveHead(0, int(line[1]))
    elif line[0] == "L":
        moveHead(0, -int(line[1]))
    elif line[0] == "U":
        moveHead(1, int(line[1]))
    elif line[0] == 'D':
        moveHead(1, -int(line[1]))

print(len(Pos1), len(Pos2))
