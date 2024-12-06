# ==================================================
# https://adventofcode.com/2024/day/5

file = open("day5.txt").read().split('\n\n')

Orders  = file[0]
Updates = file[1].split()

def IsCorrect(upd):
    good = True
    while True:
        not_swapped = True
        for i in range(len(upd)-1):
            if upd[i]+'|'+upd[i+1] not in Orders:
                upd[i], upd[i+1] = upd[i+1], upd[i]
                not_swapped = False
        if not_swapped: return good
        good = False

s1 = 0
s2 = 0
for upd in Updates:
    upd = upd.split(',')
    if IsCorrect(upd):
        s1 += int(upd[len(upd)//2])
    else:
        s2 += int(upd[len(upd)//2])

print(s1, s2)
