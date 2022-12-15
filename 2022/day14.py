# https://adventofcode.com/2022/day/14

List = open("E:\\Temp\\input14.txt").read().splitlines()
List = set(List)  # removing duplicate entries (there is a lot of them)
List = [[list(map(int, c.split(','))) for c in l.split(' -> ')] for l in List]

air = '.'
rock = '#'
source = '+'
sand = 'o'

def buildRocks(frm, to):
    frmY, toY = (frm[1], to[1]) if frm[1] < to[1] else (to[1], frm[1])
    frmX, toX = (frm[0], to[0]) if frm[0] < to[0] else (to[0], frm[0])
    for y in range(frmY, toY+1):
        for x in range(frmX-minX, toX-minX+1):
            Cave[y][x] = rock

def buildCave():
    for y in range(maxY+1):
        Cave.append([])
        for x in range(maxX-minX+1):
            if y == srcY and x == srcX:
                Cave[-1].append(source)
            else:
                Cave[-1].append(air)

    for line in List:
        for i in range(len(line)-1):
            buildRocks(line[i], line[i+1])

def spawnSand():
    sandX = srcX
    sandY = srcY
    for y in range(len(Cave)-1-srcY):
        if Cave[sandY+1][sandX] == air:
            sandY += 1
        elif sandX-1 < 0:
            # print('<< oob')
            return False
        elif Cave[sandY+1][sandX-1] == air:
            sandY += 1
            sandX -= 1
        elif sandX+1 >= len(Cave[sandY+1]):
            # print('oob >>')
            return False
        elif Cave[sandY+1][sandX+1] == air:
            sandY += 1
            sandX += 1
        else:
            Cave[sandY][sandX] = sand
            return True
    # print("fell to void")
    return False

def drawCave():
    for line in Cave:
        print(''.join(line))

def runSandSim():
    i = 0
    while Cave[srcY][srcX] == source and spawnSand():
        i += 1
    drawCave()
    return i

minX = -1
maxX = -1
maxY = -1

for l in List:
    tminX = min(l, key=lambda x: x[0])[0]
    tmaxX = max(l, key=lambda x: x[0])[0]
    tmaxY = max(l, key=lambda x: x[1])[1]
    if minX == -1 or tminX < minX: minX = tminX
    if maxX == -1 or tmaxX > maxX: maxX = tmaxX
    if maxY == -1 or tmaxY > maxY: maxY = tmaxY

srcX = 500-minX
srcY = 0

Cave = []
buildCave()
print(runSandSim())

# part 2
maxY += 2
minX = min(minX, 500-maxY)
maxX = max(maxX, 500+maxY)
List.append([[minX, maxY], [maxX, maxY]])
srcX = 500-minX

Cave = []
buildCave()
print(runSandSim())
