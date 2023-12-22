# ==================================================
# https://adventofcode.com/2023/day/14

file = open("day14.txt").read().splitlines()

States = {}

def tilt(file):
    for r in range(len(file)):
        line = ''.join(file[r]).split('#')
        for s in range(len(line)):
            c = line[s].count('O')
            line[s] = line[s].replace('O', '.').replace('.', 'O', c)
        file[r] = '#'.join(line)

def calc_load(file):
    return sum(len(row)-c for row in file for c, e in enumerate(row) if e == 'O')

def same_state(file, c):
    h = hash(tuple(file))
    if h not in States:
        States[h] = c
    elif (10**9 - c) % (c - States[h]) == 0:
        return True
    return False

file = list(zip(*file))[::-1]
tilt(file)
print(calc_load(file))

c = 0
while not same_state(file, c):
    for _ in range(4):
        tilt(file)
        file = list(zip(*file[::-1]))
    c += 1
print(calc_load(file))
