# ==================================================
# https://adventofcode.com/2024/day/4

file = open("day4.txt").read().splitlines()

def check_MAS(r, c, ro, co):
    mas = ''
    for _ in range(3):
        r += ro
        c += co
        if not (-1 < r < len(file) and -1 < c < len(file[r])):
            return 0
        mas += file[r][c]
    if mas == 'MAS':
        return 1
    return 0

def check_X(r, c):
    s = 0
    for ro in [-1, 0, 1]:
        for co in [-1, 0, 1]:
            if (ro, co) == (0, 0): continue
            s += check_MAS(r, c, ro, co)
    return s

def check_A(r, c):
    if 0 < r < len(file)-1 and 0 < c < len(file[r])-1:
        ms1 = file[r-1][c-1] + file[r+1][c+1]
        ms2 = file[r+1][c-1] + file[r-1][c+1]
        if ms1 in ('MS', 'SM') and ms2 in ('MS', 'SM'):
            return 1
    return 0

s1 = 0
s2 = 0
for r in range(len(file)):
    cX = file[r].find('X')
    while cX != -1:
        s1 += check_X(r, cX)
        cX = file[r].find('X', cX+1)
    cA = file[r].find('A')
    while cA != -1:
        s2 += check_A(r, cA)
        cA = file[r].find('A', cA+1)

print(s1, s2)
