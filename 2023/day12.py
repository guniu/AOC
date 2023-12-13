# ==================================================
# https://adventofcode.com/2023/day/12
from functools import cache

file = open("day12.txt").read().splitlines()

@cache
def solve(spr, dmg):
    if not dmg:
        if '#' in spr:
            return 0
        return 1

    cnt = 0
    rng = len(spr) - sum(dmg) - len(dmg[1:])
    brk = spr.find('#')
    if -1 < brk < rng: rng = brk

    for p in range(rng + 1):
        grp = '.'*p + '#'*dmg[0] + '.'

        for s, g in zip(spr, grp):
            if s != '?' and s != g: break
        else:
            cnt += solve(spr[len(grp):], dmg[1:])
    return cnt

s1 = 0
s2 = 0
for line in file:
    spr, dmg = line.split()
    dmg = tuple(map(int, dmg.split(',')))
    s1 += solve(spr, dmg)
    s2 += solve('?'.join((spr,)*5), dmg*5)
print(s1, s2)
