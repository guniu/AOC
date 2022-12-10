# https://adventofcode.com/2022/day/6

List = open("E:\\Temp\\input6.txt").read()

print([i+4 for i in range(len(List)) if len(set(List[i:i+4])) == 4][0])
print([i+14 for i in range(len(List)) if len(set(List[i:i+14])) == 14][0])
