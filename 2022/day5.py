# https://adventofcode.com/2022/day/5

# import time
# def printStack(Stack):
#     stackHeight = max(map(len, Stack))
#     for h in range(stackHeight, 0, -1):
#         line = ""
#         for S in Stack:
#             if len(S) < h:
#                 line += "    "
#             else:
#                 line += f" [{S[h-1]}]"
#         print(line[1:])

List = open("E:\\Temp\\input5.txt").read().split('\n\n')
Stacklines = List[0].split('\n')
List = List[1].split('\n')

Stack = [[] for x in Stacklines.pop().split()]

for line in Stacklines[::-1]:
    for i in range(1, len(line), 4):
        if line[i].isalpha():
            Stack[(i-1)//4].append(line[i])
# printStack(Stack)

Stack2 = list(map(list.copy, Stack))
for line in List:
    line = line.split()
    amt = -int(line[1])
    frm = int(line[3])-1
    to = int(line[5])-1

    Stack[to].extend(Stack[frm][:amt-1:-1])
    Stack[frm][amt:] = []
    # print('\n'*5)
    # printStack(Stack)
    # time.sleep(0.01)
    Stack2[to].extend(Stack2[frm][amt:])
    Stack2[frm][amt:] = []
print(''.join(x[-1] for x in Stack if x), ''.join(x[-1] for x in Stack2 if x))
