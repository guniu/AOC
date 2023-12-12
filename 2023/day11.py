# ==================================================
# https://adventofcode.com/2023/day/11

file = open("day11.txt").read().splitlines()

def expand(file, E):
    for r in range(len(file)):
        if file[r].find('#') == -1:
            E.append(r)

Er = []
expand(file, Er)
Ec = []
expand(list(map(''.join, zip(*file))), Ec)

G = []
for r in range(len(file)):
    c = file[r].find('#')
    while c != -1:
        er = sum(1 for e in Er if e < r)
        ec = sum(1 for e in Ec if e < c)
        G.append([r, c, er, ec])
        c = file[r].find('#', c+1)

P = [g2[0]+g2[2]-g1[0]-g1[2] + abs(g2[1]+g2[3]-g1[1]-g1[3]) for i, g1 in enumerate(G) for g2 in G[i+1:]]
print(sum(P))

n = 10**6 - 1
P = [g2[0]+g2[2]*n-g1[0]-g1[2]*n + abs(g2[1]+g2[3]*n-g1[1]-g1[3]*n) for i, g1 in enumerate(G) for g2 in G[i+1:]]
print(sum(P))
