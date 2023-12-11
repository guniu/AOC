# ==================================================
# https://adventofcode.com/2023/day/10

Pipes = open("day10.txt").read().splitlines()

for r, line in enumerate(Pipes):
    if (c := line.find('S')) != -1:
        S = [r, c]
        break

P = {'|': 'ns', '-': 'ew', 'L': 'ne', 'J': 'nw', '7': 'sw', 'F': 'se', '.': ''}

def Dir(r, c):
    return P[Pipes[r][c]]

C = []
D = []
if 's' in Dir(S[0]-1, S[1]):
    C.append([S[0]-1, S[1]])
    D.append(['s'])
    P['S'] = P.get('S', '')+'n'
if 'n' in Dir(S[0]+1, S[1]):
    C.append([S[0]+1, S[1]])
    D.append(['n'])
    P['S'] = P.get('S', '')+'s'
if 'w' in Dir(S[0], S[1]+1):
    C.append([S[0], S[1]+1])
    D.append(['w'])
    P['S'] = P.get('S', '')+'e'
if 'e' in Dir(S[0], S[1]-1):
    C.append([S[0], S[1]-1])
    D.append(['e'])
    P['S'] = P.get('S', '')+'w'

def add_Loop(c, d):
    if d == 'ns':
        Loop.append(c+[1])
    elif 'n' in d:
        Loop.append(c+[2])
    elif 's' in d:
        Loop.append(c+[3])

def next_pipe(c, d):
    go = Dir(c[0], c[1])
    add_Loop(c, go)
    go = go.replace(d[0], '')
    if go == 'n':
        c[0] -= 1
        d[0] = 's'
    elif go == 's':
        c[0] += 1
        d[0] = 'n'
    elif go == 'e':
        c[1] += 1
        d[0] = 'w'
    elif go == 'w':
        c[1] -= 1
        d[0] = 'e'

Loop = []
i = 1
while C[0] != C[1]:
    next_pipe(C[0], D[0])
    next_pipe(C[1], D[1])
    i += 1
print(i)

add_Loop(C[0], Dir(C[0][0], C[0][1]))
add_Loop(S, P['S'])
Loop.sort()

IN = False
s = 0
x = 0
i = 0
for p in Loop:
    if IN and not s:
        i += p[1]-x-1

    if p[2] == 1:
        IN = not IN
    elif s and s != p[2]:
        IN = not IN
        s = 0
    elif s == p[2]:
        s = 0
    else:
        s = p[2]

    if IN: x = p[1]
print(i)
