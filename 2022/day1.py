# https://adventofcode.com/2022/day/1

List = open("E:\\Temp\\input1.txt").read().split('\n\n')

arr = [list(map(int, x.splitlines())) for x in List]

top = max(arr, key=lambda x: sum(x))
print("part 1: ", sum(top))

topThree = []
for i in range(3):
    topOne = arr.index(max(arr, key=lambda x: sum(x)))
    topThree.append(arr.pop(topOne))
print("part 2: ", sum(map(sum, topThree)))
