# ==================================================
# https://adventofcode.com/2023/day/2

file = open("E:\\Temp\\AOC2023\\day2.txt").read().splitlines()

Cubes = {'red': 12, 'green': 13, 'blue': 14}

IDsum = 0
Psum = 0

for line in file:
    line = line.split(':')
    gameID = int(line[0].split()[1])
    c = line[1].replace(',', '').replace(';', '').split()
    P = {}

    for i in range(0, len(c), 2):
        if Cubes[c[i+1]] < int(c[i]):
            gameID = 0
        P[c[i+1]] = max(int(c[i]), P.get(c[i+1], 0))

    IDsum += gameID
    k = 1
    for v in P.values():
        k *= v
    Psum += k

print(IDsum, Psum)
