# https://adventofcode.com/2022/day/4

List = open("E:\\Temp\\input4.txt")

count1 = 0
count2 = 0
for line in List:
    n = list(map(int, line.replace(',', '-').split('-')))
    if n[0] >= n[2] and n[1] <= n[3] or n[2] >= n[0] and n[3] <= n[1]: count1 += 1
    if n[2] <= n[0] <= n[3] or n[0] <= n[2] <= n[1]: count2 += 1

    # a = set(range(n[0], n[1]+1))
    # b = set(range(n[2], n[3]+1))
    # if a.issubset(b) or a.issuperset(b): count1 += 1
    # if a.intersection(b): count2 += 1

    # a = range(n[0], n[1]+1)
    # b = range(n[2], n[3]+1)
    # if n[0] in b and n[1] in b or n[2] in a and n[3] in a: count1 += 1
    # if n[0] in b or n[2] in a: count2 += 1

print(count1, count2)
