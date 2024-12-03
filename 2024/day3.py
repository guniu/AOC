# ==================================================
# https://adventofcode.com/2024/day/3

file = open("day3.txt").read()

def get_mul(i):
    j = file.find(',', i)
    if not file[i:j].isdecimal():
        return 0
    num1 = int(file[i:j])
    i = j+1
    j = file.find(')', i)
    if not file[i:j].isdecimal():
        return 0
    return num1*int(file[i:j])

mul_index = file.find('mul(')
s1 = 0
s2 = 0
while mul_index != -1:
    mul = get_mul(mul_index+4)
    s1 += mul
    dont = file.rfind('don\'t()', 0, mul_index)
    do = file.rfind('do()', 0, mul_index)
    if do >= dont:
        s2 += mul
    mul_index = file.find('mul(', mul_index+4)

print(s1, s2)
