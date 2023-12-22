# ==================================================
# https://adventofcode.com/2023/day/15

file = open("day15.txt").read().strip().split(',')

def hush(step):
    res = 0
    for c in step:
        res = ((res + ord(c)) * 17) % 256
    return res

p1 = 0
Boxes = {}
for step in file:
    p1 += hush(step)

    label, fl = step.replace('=', '-').split('-')
    box = hush(label)

    if box not in Boxes:
        if fl: Boxes[box] = {label: int(fl)}
    elif fl:
        Boxes[box][label] = int(fl)
    elif label in Boxes[box]:
        del Boxes[box][label]

print(p1)

print(sum((b+1)*i*f for b, l in Boxes.items() for i, f in enumerate(l.values(), 1)))
