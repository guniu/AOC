# ==================================================
# https://adventofcode.com/2024/day/7

file = open("day7.txt").read().splitlines()

def TestEquation(test, nums):
    op = len(nums)-1
    for c in range(2**op):
        for p in range(2**op):
            if c & p: continue
            eq = nums[0]
            b = 1 << (op-1)
            for num in nums[1:]:
                if c & b:
                    eq = int(f'{eq}{num}')
                elif p & b:
                    eq *= num
                else:
                    eq += num
                b >>= 1
            if eq == test: return c
    return -1

p1 = 0
p2 = 0
for line in file:
    line = line.replace(':', '').split()
    test = int(line[0])
    nums = list(map(int, line[1:]))
    c = TestEquation(test, nums)
    if c == 0:
        p1 += test
        p2 += test
    elif c > 0:
        p2 += test

print(p1, p2)
