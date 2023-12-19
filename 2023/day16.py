# ==================================================
# https://adventofcode.com/2023/day/16

file = open("day16.txt").read().splitlines()

rt = (0, 1)
lt = (0, -1)
dn = (1, 0)
up = (-1, 0)

M = {'/': {rt: [up], lt: [dn], dn: [lt], up: [rt]},
     '\\': {rt: [dn], lt: [up], dn: [rt], up: [lt]},
     '|': {rt: [dn, up], lt: [dn, up], dn: [dn], up: [up]},
     '-': {rt: [rt], lt: [lt], dn: [rt, lt], up: [rt, lt]}}

def isValid(r, c, d, P):
    r += d[0]
    c += d[1]
    if 0 <= r < len(file) and 0 <= c < len(file[r]):
        t = (r, c, abs(d[0]))
        if t not in P or file[r][c] in '/\\':
            P.add(t)
            return True
    return False

def run_beam(sr, sc, sd):
    P = {(sr, sc, abs(sd[0]))}
    Q = [(sr, sc, sd)]
    while Q:
        r, c, d = Q.pop(0)
        s = file[r][c]
        if s != '.':
            for nd in M[s][d]:
                if isValid(r, c, nd, P):
                    Q.append((r+nd[0], c+nd[1], nd))
        elif isValid(r, c, d, P):
            Q.append((r+d[0], c+d[1], d))
    return len({(f[0], f[1]) for f in P})

max_en = 0
for r in range(len(file)):
    en1 = run_beam(r, 0, rt)
    if r == 0: print(en1)
    en2 = run_beam(r, len(file[r])-1, lt)
    max_en = max(max_en, en1, en2)
for c in range(len(file[0])):
    en1 = run_beam(0, c, dn)
    en2 = run_beam(len(file)-1, c, up)
    max_en = max(max_en, en1, en2)
print(max_en)
