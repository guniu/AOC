# ==================================================
# https://adventofcode.com/2023/day/9

file = open("day9.txt").read().splitlines()

History = [list(map(int, line.split())) for line in file]

Next = []
Prev = []

def get_diff(seq):
    return [y-x for x, y in zip(seq, seq[1:])]

for seq in History:
    Diff = []
    while any(seq):
        Diff.append(seq)
        seq = get_diff(seq)

    Next.append(sum(x[-1] for x in Diff))

    s = 0
    for x in Diff[::-1]:
        s = x[0] - s
    Prev.append(s)

print(sum(Next))
print(sum(Prev))
