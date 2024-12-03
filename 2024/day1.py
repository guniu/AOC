# ==================================================
# https://adventofcode.com/2024/day/1

file = open("day1.txt").read().splitlines()

l1 = []
l2 = []

for pair in file:
    pair = pair.split()
    l1.append(int(pair[0]))
    l2.append(int(pair[1]))

l1.sort()
l2.sort()

p1 = 0
p2 = 0
for i, ID in enumerate(l1):
    p1 += abs(ID - l2[i])
    p2 += ID * l2.count(ID)

print(p1, p2)
