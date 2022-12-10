# https://adventofcode.com/2022/day/2

List = open("E:\\Temp\\input2.txt").read().split('\n')

lose     = 0
draw     = 3
win      = 6
rock     = 1
paper    = 2
scissors = 3

Games = {"A X": draw+rock, "A Y": win+paper,  "A Z": lose+scissors,
         "B X": lose+rock, "B Y": draw+paper, "B Z": win+scissors,
         "C X": win+rock,  "C Y": lose+paper, "C Z": draw+scissors}

def Swap(r):
    if r[0] == "A":
        if r[2] == "X":
            r = "A Z"
        elif r[2] == "Y":
            r = "A X"
        elif r[2] == "Z":
            r = "A Y"
    elif r[0] == "C":
        if r[2] == "X":
            r = "C Y"
        elif r[2] == "Y":
            r = "C Z"
        elif r[2] == "Z":
            r = "C X"
    return r

count1 = 0
count2 = 0
for r in List:
    count1 += Games[r]
    count2 += Games[Swap(r)]

print(count1, count2)
