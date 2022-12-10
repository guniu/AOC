# https://adventofcode.com/2022/day/3

List = open("E:\\Temp\\input3.txt").read().split('\n')

count1 = 0
for line in List:
    c = set(line[:len(line)//2]).intersection(line[len(line)//2:]).pop()
    count1 += ord(c) - (ord('a')-1 if c.islower() else ord('A')-27)
print(count1)

count2 = 0
for i in range(0, len(List), 3):
    c = set(List[i]).intersection(List[i+1]).intersection(List[i+2]).pop()
    count2 += ord(c) - (ord('a')-1 if c.islower() else ord('A')-27)
print(count2)
