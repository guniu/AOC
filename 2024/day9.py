# ==================================================
# https://adventofcode.com/2024/day/9

file = open("day9.txt").read().strip()
disk = list(map(int, file))

backID = (len(disk)-1)//2

empty1 = disk[1::2]
eID = 0
p1 = disk[0]
step = 1
s1 = 0

empty2 = disk[1::2]
I = {f: 0 for f in range(1, 10)}
S = [p := 0] + [p := p+b for b in disk[:-1]]
s2 = 0

for f in disk[backID*2::-2]:
    b = f
    while b > 0:
        while eID < backID and empty1[eID] == 0:
            eID += 1
            p1 += disk[eID*2]

        if eID < backID:
            k = min(empty1[eID], b)
            empty1[eID] -= k
            b -= k
        else:
            if step == 1:
                if f == b:
                    p1 -= disk[backID*2+1]-empty1[backID]+1
                else:
                    p1 -= f-b+1
                step = -1
            else:
                p1 -= disk[backID*2+1]
            k = -b
            b = 0

        for p1 in range(p1, p1+k, step):
            s1 += p1 * backID
        p1 += step

    for i in range(I[f], backID):
        if empty2[i] >= f:
            I[f] = i
            p2 = S[i*2+2] - empty2[i]
            empty2[i] -= f
            break
    else:
        p2 = S[backID*2]

    for p2 in range(p2, p2+f):
        s2 += p2 * backID

    backID -= 1

print(s1, s2)
