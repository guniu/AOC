# https://adventofcode.com/2022/day/7

List = open("E:\\Temp\\input7.txt")

currentDir = [[]]
dirSizes = []

for line in List:
    line = line.split()
    if line[:2] == ['$', 'cd']:
        if line[2] != '..':
            currentDir[-1].append([0])
            currentDir.append(currentDir[-1][-1])
        else:
            dirSizes.append(currentDir.pop()[0])
            currentDir[-1][0] += dirSizes[-1]
    elif line[0].isdecimal():
        currentDir[-1][0] += int(line[0])

if len(currentDir) > 2:
    for i in range(len(currentDir)-2):
        dirSizes.append(currentDir.pop()[0])
        currentDir[-1][0] += dirSizes[-1]

total = currentDir[-1][0]
dirSizes.append(total)

maxsize = 70000000
free = 30000000
needed = total + free - maxsize

print(sum([s for s in dirSizes if s <= 100000]))
print(min([s for s in dirSizes if s >= needed]) if needed > 0 else 0)
