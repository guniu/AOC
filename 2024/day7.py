# ==================================================
# https://adventofcode.com/2024/day/7

file = open("day7.txt").read().splitlines()

def TestEq(t, n):
    if len(n) == 1: return t == n[0]
    r = TestEq(t, (n[0]+n[1],)+n[2:])
    if r: return r
    r = TestEq(t, (n[0]*n[1],)+n[2:])
    if r: return r
    if TestEq(t, (int(f'{n[0]}{n[1]}'),)+n[2:]):
        return 2
    return False

p1 = 0
p2 = 0
for line in file:
    test, nums = line.split(': ')
    test = int(test)
    nums = tuple(map(int, nums.split()))
    r = TestEq(test, nums)
    if r == 2:
        p2 += test
    elif r:
        p1 += test
        p2 += test

print(p1, p2)
