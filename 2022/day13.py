# https://adventofcode.com/2022/day/13

List = open("E:\\Temp\\input13.txt").read().split('\n\n')
List = [list(map(eval, p.splitlines())) for p in List]

def compareValues(v1, v2):
    if isinstance(v1, int) and isinstance(v2, int):
        if v1 < v2: return 1
        elif v1 > v2: return 2
        else: return 0
    elif isinstance(v1, int):
        v1 = [v1]
    elif isinstance(v2, int):
        v2 = [v2]
    return compareArrays(v1, v2)

def compareArrays(a1, a2):
    for i in range(len(a1)):
        if i <= len(a2)-1:
            comp = compareValues(a1[i], a2[i])
            if comp: return comp
        else: return 2
    if len(a1) < len(a2): return 1
    return 0

ro = [p+1 for p, pair in enumerate(List) if compareArrays(pair[0], pair[1]) == 1]
print('sum:', sum(ro))

List2 = [p for pair in List for p in pair]
div1 = [[2]]
div2 = [[6]]
List2.extend([div1, div2])

for i in range(len(List2)):
    for j in range(len(List2)-1-i):
        if compareArrays(List2[j], List2[j+1]) == 2:
            List2[j], List2[j+1] = List2[j+1], List2[j]

i1 = List2.index(div1)+1
i2 = List2.index(div2)+1
print(i1*i2)
