# ==================================================
# https://adventofcode.com/2024/day/2

file = open("day2.txt").read().splitlines()

reports = [list(map(int, r.split())) for r in file]

def isSafe(rep):
    inc = -1
    for i in range(len(rep)-1):
        diff = rep[i+1] - rep[i]
        if inc == -1:
            inc = 1 if diff > 0 else 0
        else:
            inc2 = 1 if diff > 0 else 0
            if inc != inc2: return False
        diff = abs(diff)
        if not 1 <= diff <= 3:
            return False
    return True

s1 = 0
s2 = 0
for rep in reports:
    if isSafe(rep):
        s1 += 1
        s2 += 1
        continue
    for j in range(len(rep)):
        modrep = rep.copy()
        modrep.pop(j)
        if isSafe(modrep):
            s2 += 1
            break

print(s1, s2)
