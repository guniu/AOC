# ==================================================
# https://adventofcode.com/2023/day/8

from math import lcm

file = open("day8.txt").read().splitlines()

I = [0 if d == 'L' else 1 for d in file[0]]
N = {}
for line in file[2:]:
    line = line.replace(' = (', ', ').replace(')', '').split(', ')
    N[line[0]] = [line[1], line[2]]

curr = 'AAA'
i = 0
while curr != 'ZZZ':
    curr = N[curr][I[i % len(I)]]
    i += 1
print(i)

curr = [k for k in N.keys() if k[-1] == 'A']
dist = [0]*len(curr)
i = 0
while 0 in dist:
    for n in range(len(curr)):
        curr[n] = N[curr[n]][I[i % len(I)]]
        if curr[n][-1] == 'Z' and dist[n] == 0:
            dist[n] = i+1
    i += 1
print(lcm(*dist))
