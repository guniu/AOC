# ==================================================
# https://adventofcode.com/2023/day/3

file  = open("day3.txt").read().splitlines()

C     = [[] for _ in file]
nums  = []
gears = []
g     = 0

def check_for_digit(r, c):
    global g
    if r < 0 or r >= len(file) or c < 0 or c >= len(file[r]):
        return

    if file[r][c].isdigit() and c not in C[r]:
        while c > 0 and file[r][c-1].isdigit(): c -= 1
        n = ''
        while c < len(file[r]) and file[r][c].isdigit():
            n += file[r][c]
            C[r].append(c)
            c += 1
        nums.append(int(n))
        g += 1

for r in range(len(file)):
    for c in range(len(file[r])):
        if file[r][c] != '.' and not file[r][c].isdigit():
            check_for_digit(r-1, c)
            check_for_digit(r-1, c-1)
            check_for_digit(r-1, c+1)

            check_for_digit(r, c-1)
            check_for_digit(r, c+1)

            check_for_digit(r+1, c)
            check_for_digit(r+1, c-1)
            check_for_digit(r+1, c+1)

            if file[r][c] == '*' and g == 2:
                gears.append(nums[-1] * nums[-2])
            g = 0

print(sum(nums), sum(gears))
