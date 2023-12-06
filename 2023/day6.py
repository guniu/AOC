# ==================================================
# https://adventofcode.com/2023/day/6

from math import sqrt, ceil

file  = open("day6.txt").read().splitlines()

Times = file[0].split()[1:]
Dists = file[1].split()[1:]

# def get_wins(t, d):
#     t, d = int(t), int(d)
#     i = 1
#     while i*(t-i) <= d:
#         i += 1
#     return t-i-i+1

def get_wins(t, d):
    t, d = int(t), int(d)
    q  = sqrt(t**2 - 4*d)
    x1 = int((t-q)/2)+1
    x2 = ceil((t+q)/2)-1
    return x2-x1+1

wins = 1
for t, d in zip(Times, Dists):
    wins *= get_wins(t, d)
print(wins)

print(get_wins(''.join(Times), ''.join(Dists)))
