# https://adventofcode.com/2022/day/8

List = open("E:\\Temp\\input8.txt").read().split('\n')

outer = len(List[0])*2+(len(List)-2)*2

def isVisible(tree, row, col):
    leftV = True
    for c, t in enumerate(List[row]):
        if c < col and leftV:
            if int(t) >= tree:
                leftV = False
        elif c > col:
            if leftV: return True
            if int(t) >= tree:
                break
    else:
        return True

    upV = True
    for r, t in enumerate(List):
        t = t[col]
        if r < row and upV:
            if int(t) >= tree:
                upV = False
        elif r > row:
            if upV: return True
            if int(t) >= tree:
                break
    else:
        return True

    return False

def calcScore(tree, row, col):
    left = col
    right = len(List[row])-col-1
    for c, t in enumerate(List[row]):
        if c < col:
            if int(t) >= tree:
                left = col-c
        elif c > col:
            if int(t) >= tree:
                right = c-col
                break

    up = row
    down = len(List)-row-1
    for r, t in enumerate(List):
        t = t[col]
        if r < row:
            if int(t) >= tree:
                up = row-r
        elif r > row:
            if int(t) >= tree:
                down = r-row
                break

    return left*right*up*down

count = 0
maxscore = 0
for row, line in enumerate(List[1:-1]):
    for col, tree in enumerate(line[1:-1]):
        if isVisible(int(tree), row+1, col+1):
            count += 1
        score = calcScore(int(tree), row+1, col+1)
        if score > maxscore:
            maxscore = score

print(outer+count)
print(maxscore)
