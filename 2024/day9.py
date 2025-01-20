# ==================================================
# https://adventofcode.com/2024/day/9

file = open("day9.txt").read().strip()
disk = list(map(int, file))

backID = (len(disk)-1)//2
Pos = [p := 0] + [p := p+b for b in disk]

empty1 = disk[1::2]
eID = 0
s1 = 0

empty2 = disk[1::2]
Idx = [0]*10
s2 = 0

for f in disk[backID*2::-2]:
    b = f
    while b > 0:
        while eID < backID and empty1[eID] == 0:
            eID += 1
        if eID < backID:
            p1 = Pos[eID*2+2] - empty1[eID]
            k = min(empty1[eID], b)
            empty1[eID] -= k
            b -= k
        else:
            p1 = Pos[backID*2]
            k = b
            b = 0
        s1 += (2*p1 + k-1) * k // 2 * backID

    for i in range(max(Idx[:f+1]), backID):
        if empty2[i] >= f:
            Idx[f] = i
            p2 = Pos[i*2+2] - empty2[i]
            empty2[i] -= f
            break
    else:
        if i == backID-1: Idx[f] = backID
        p2 = Pos[backID*2]
    s2 += (2*p2 + f-1) * f // 2 * backID

    backID -= 1

print(s1, s2)
