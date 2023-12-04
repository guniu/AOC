# ==================================================
# https://adventofcode.com/2023/day/4

file  = open("day4.txt").read().splitlines()

total = 0
D = [1] * len(file)

for i, line in enumerate(file):
    win  = set(line.split(':')[1].split('|')[0].split())
    mine = set(line.split('|')[1].split())
    w = len(mine.intersection(win))
    if w:
        total += 2**(w-1)

        for n in range(1, w+1):
            D[i+n] += D[i]

print(total, sum(D))
