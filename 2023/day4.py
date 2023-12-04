# ==================================================
# https://adventofcode.com/2023/day/4

file  = open("day4.txt").read().splitlines()

total = 0
D = dict()

for i, line in enumerate(file, 1):
    win  = set(line.split(':')[1].split('|')[0].split())
    mine = set(line.split('|')[1].split())
    w = len(mine.intersection(win))
    if w:
        total += 2**(w-1)

        for n in range(1, w+1):
            D[i+n] = D.get(i+n, 0) + 1 + D.get(i, 0)

print(total, sum(D.values())+len(file))
