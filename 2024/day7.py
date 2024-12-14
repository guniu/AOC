# ==================================================
# https://adventofcode.com/2024/day/7

file = open("day7.txt").read().splitlines()

def TestEq(t, n):
    if len(n) == 1: return t == n[0]
    r = TestEq(t-n[-1], n[:-1])
    if r: return r
    r = t % n[-1] == 0 and TestEq(t//n[-1], n[:-1])
    if r: return r
    s = 10**len(str(n[-1]))
    if t % s == n[-1] and TestEq(t//s, n[:-1]):
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
