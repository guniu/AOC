# https://adventofcode.com/2022/day/15

List = open("E:\\Temp\\input15.txt").read().splitlines()
for i in range(len(List)):
    line = List[i].replace('=', ' ').replace(',', '').replace(':', '').split()
    line = [int(line[3]), int(line[5]), int(line[11]), int(line[13])]
    line.append(abs(line[0]-line[2])+abs(line[1]-line[3]))
    List[i] = line

exclude = set()
def get_Y_ranges(Y):
    Y_ranges = []
    for s in List:
        dist_to_B = s[4]
        dist_to_Y = abs(s[1]-Y)
        if dist_to_B >= dist_to_Y:
            r = dist_to_B - dist_to_Y
            Y_ranges.append([s[0]-r, s[0]+r])
            if s[3] == Y: exclude.add(s[2])
    return sorted(Y_ranges)

def get_X_gap(Y_ranges, X=0):
    for r in Y_ranges:
        if r[0] <= X <= r[1]:
            X = r[1]+1
    return X

part1_Y = 2000000

Y_ranges = get_Y_ranges(part1_Y)
minX = Y_ranges[0][0]
maxX = max(Y_ranges, key=lambda k: k[1])[1]

X = get_X_gap(Y_ranges, minX)
pos = X-minX
while X <= maxX:
    minX = X+1
    X = get_X_gap(Y_ranges, minX)
    pos += X-minX

print('part 1:', pos-len(exclude))

MAX = 4000000
div = MAX//100
for Y in range(MAX+1):
    if Y % div == 0: print('Searching:', Y//div, '%')
    X = get_X_gap(get_Y_ranges(Y))
    if X <= MAX:
        print('Found one at x:', X, 'y:', Y, 'part 2:', X*MAX+Y)
