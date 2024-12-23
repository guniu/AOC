# ==================================================
# https://adventofcode.com/2024/day/8

file = open("day8.txt").read().splitlines()

A = {}
Rs = len(file)
Cs = len(file[0])

for r in range(Rs):
    for c, a in enumerate(file[r]):
        if a != '.':
            A[a] = A.get(a, []) + [(r, c)]

N1 = set()
N2 = set()
for a in A.values():
    for i, (r1, c1) in enumerate(a[:-1]):
        for r2, c2 in a[i+1:]:
            rd = r2-r1
            cd = c2-c1
            j = 0
            jd = 1
            while True:
                ar = r1-j*rd
                ac = c1-j*cd
                if -1 < ar < Rs and -1 < ac < Cs:
                    if j == 1 or j == -2:
                        N1.add((ar, ac))
                    N2.add((ar, ac))
                else:
                    if j < 0: break
                    j = 0
                    jd = -1
                j += jd

print(len(N1), len(N2))
