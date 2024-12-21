# ==================================================
# https://adventofcode.com/2024/day/6

file = open("day6.txt").read().splitlines()

O = set()

for r in range(len(file)):
    c = file[r].find('^')
    if c != -1:
        sR = r
        sC = c
    c = file[r].find('#')
    while c != -1:
        O.add((r, c))
        c = file[r].find('#', c+1)

def ChangeDir(d):
    if d[0] != 0:
        return (0, -d[0])
    else:
        return (d[1], 0)

RLen = len(file)
CLen = len(file[0])

def GetPath(O, p2=False):
    r = sR
    c = sC
    d = (-1, 0)
    P = set()
    while -1 < r < RLen and -1 < c < CLen:
        if (r, c, d) in P:
            return 1
        P.add((r, c, d))
        tr = r+d[0]
        tc = c+d[1]
        if (tr, tc) in O:
            d = ChangeDir(d)
        else:
            r = tr
            c = tc
    return 0 if p2 else {p[:2] for p in P}

P = GetPath(O)
print(len(P))

print(sum(GetPath(O | {o}, True) for o in P if o != (sR, sC)))
