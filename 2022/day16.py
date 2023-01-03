# https://adventofcode.com/2022/day/16

List = open("E:\\Temp\\input16.txt")

class Valve:
    state = 1

    def __init__(self, name, flow, nbr):
        self.name = name
        self.flow = flow
        self.nbr  = nbr
        self.dist = set()
        if flow:
            self.state = Valve.state
            Valve.state <<= 1

    def __repr__(self):
        # nbr = type(self.nbr)(n.name if isinstance(n, Valve) else n for n in self.nbr)
        return f'V({self.name}, {self.flow})'

V = {}
for line in List:
    line = line.replace('=', ' ').replace(';', '').replace(',', '').split()
    V[line[1]] = Valve(line[1], int(line[5]), set(line[10:]))

AA = V['AA']

FV = [AA]
for v in V.values():
    v.nbr = {V[n] for n in v.nbr}
    if v.flow: FV.append(v)

for fv in FV:
    Q = [(fv, 0)]
    P = {fv}
    while Q:
        v, d = Q.pop(0)
        if v.flow and d: fv.dist.add((v, d+1))
        for n in v.nbr:
            if n not in P:
                Q.append((n, d+1))
                P.add(n)

def search(N, T, S, s=0, f=0):
    if f > S.get(s, 0): S[s] = f
    for v, t in N.dist:
        if not s & v.state and T-t > 0:
            search(v, T-t, S, s | v.state, f+(T-t)*v.flow)
    return S

print(max(search(AA, 30, {}).values()))

S = list(search(AA, 26, {}).items())
p2 = max(f1+f2 for i, (s1, f1) in enumerate(S) for s2, f2 in S[i+1:] if not s1 & s2)
print(p2)
