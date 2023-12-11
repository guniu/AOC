# ==================================================
# https://adventofcode.com/2023/day/11

file = open("day11.txt").read().splitlines()

def expand(file, M):
    i = 0
    for r in range(len(file)):
        r += i
        if file[r].find('#') != -1:
            continue
        file.insert(r, '.'*len(file[r]))
        M.append(r)
        i += 1

Mr = []
expand(file, Mr)
file = list(map(''.join, zip(*file)))
Mc = []
expand(file, Mc)
file = list(map(''.join, zip(*file)))

G = []
for r in range(len(file)):
    c = file[r].find('#')
    while c != -1:
        G.append([r, c])
        c = file[r].find('#', c+1)

P = [abs(g2[0]-g1[0]) + abs(g2[1]-g1[1]) for i, g1 in enumerate(G) for g2 in G[i+1:]]
print(sum(P))

n = 10**6 - 2
P2 = []
for i, g1 in enumerate(G):
    for g2 in G[i+1:]:
        m = 0
        for r in Mr:
            if g1[0] < r < g2[0] or g2[0] < r < g1[0]:
                m += n
        for c in Mc:
            if g1[1] < c < g2[1] or g2[1] < c < g1[1]:
                m += n
        P2.append(abs(g2[0]-g1[0]) + abs(g2[1]-g1[1]) + m)
print(sum(P2))
