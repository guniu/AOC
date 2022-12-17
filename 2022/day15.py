# https://adventofcode.com/2022/day/15

List = open("E:\\Temp\\input15.txt").read().splitlines()
for i in range(len(List)):
    line = List[i].replace('Sensor at x=', '')
    line = line.replace(', y=', ' ')
    line = line.replace(': closest beacon is at x=', ' ')
    List[i] = list(map(int, line.split()))

exclude = set()
def get_Y_ranges(Y):
    Y_ranges = []
    for s in List:
        dist_to_B = abs(s[0]-s[2])+abs(s[1]-s[3])
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
for Y in range(0, MAX+1):
    if Y % div == 0: print('Searching:', Y//div, '%')
    X = get_X_gap(get_Y_ranges(Y))
    if X <= MAX:
        print('Found one at x:', X, 'y:', Y, 'part 2:', X*MAX+Y)
