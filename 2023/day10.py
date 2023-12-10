# ==================================================
# https://adventofcode.com/2023/day/10

Pipes = open("day10.txt").read().splitlines()

for r, line in enumerate(Pipes):
    if (c := line.find('S')) != -1:
        S = [r, c]
        break

Loop = [S]
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

def next_pipe(c, d):
    go = Dir(c[0], c[1]).replace(d[0], '')
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

i = 1
while C[0] != C[1]:
    Loop.append(C[0].copy())
    Loop.append(C[1].copy())
    next_pipe(C[0], D[0])
    next_pipe(C[1], D[1])
    i += 1
Loop.append(C[0].copy())
print(i)

i = 0
IN = False
A = ''
for r in range(len(Pipes)):
    for c, p in enumerate(Pipes[r]):
        if [r, c] in Loop:
            if 'n' in P[p]:
                if A == 's':
                    IN = not IN
                    A = ''
                elif A: A = ''
                else: A = 'n'
            if 's' in P[p]:
                if A == 'n':
                    IN = not IN
                    A = ''
                elif A: A = ''
                else: A = 's'
        elif IN:
            i += 1
print(i)
