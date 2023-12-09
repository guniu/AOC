# ==================================================
# https://adventofcode.com/2023/day/9

file = open("day9.txt").read().splitlines()

History = [list(map(int, line.split())) for line in file]

Next = []
Prev = []

for seq in History:
    Diff = []
    while any(seq):
        Diff.append(seq)
        seq = [y-x for x, y in zip(seq, seq[1:])]

    s1 = 0
    s2 = 0
    for x in Diff[::-1]:
        s1 += x[-1]
        s2 = x[0] - s2
    Next.append(s1)
    Prev.append(s2)

print(sum(Next))
print(sum(Prev))
