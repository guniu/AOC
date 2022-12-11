# https://adventofcode.com/2022/day/11

List = open("E:\\Temp\\input11.txt").read().split('\n\n')
List = [m.splitlines() for m in List]

multiDiv = 1
for m in List:
    m[0] = 0
    m[1] = list(map(int, m[1].split(': ')[-1].split(', ')))
    m[2] = m[2].split('= ')[-1]
    m[3] = int(m[3].split()[-1])
    m[4] = int(m[4].split()[-1])
    m[5] = int(m[5].split()[-1])
    multiDiv *= m[3]
    # print(m)

def monkey_business(part, rounds):
    for _ in range(rounds):
        for monkey in List:
            for old in monkey[1]:
                monkey[0] += 1
                if part == 1: new = eval(monkey[2])//3
                else:         new = eval(monkey[2])%multiDiv
                List[monkey[5 if new%monkey[3] else 4]][1].append(new)
            monkey[1].clear()

    ins = sorted([m[0] for m in List])
    print(ins[-2]*ins[-1])

# monkey_business(1, 20)
monkey_business(2, 10000)
