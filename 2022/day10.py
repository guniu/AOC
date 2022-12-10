# https://adventofcode.com/2022/day/10

List = open("E:\\Temp\\input10.txt")

Cycles = range(20, 221, 40)
cycle = 0
sigSum = 0
X = 1

def tick():
    global cycle, sigSum
    cycle += 1
    if cycle in Cycles: sigSum += X*cycle
    print('#' if abs(X-(cycle-1)%40) <= 1 else '.', end='' if cycle%40 else '\n')

for line in List:
    line = line.split()
    if line[0] == "addx":
        for _ in range(2):
            tick()
        X += int(line[1])
    elif line[0] == "noop":
        tick()
List.close()

print(sigSum)
