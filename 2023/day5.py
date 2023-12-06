# ==================================================
# https://adventofcode.com/2023/day/5

file  = open("day5.txt").read().split('\n\n')

seeds = [int(s) for s in file[0].split()[1:]]
maps  = [[[int(n) for n in l.split()] for l in seg.splitlines()[1:]] for seg in file[1:]]

for i in range(len(maps)):
    for l in maps[i]:
        l[0] -= l[1]
        l[2] += l[1]
    # maps[i] = sorted(maps[i], key=lambda k: k[1])

loc = []
for s in seeds:
    for m in maps:
        for l in m:
            if l[1] <= s < l[2]:
                s += l[0]
                break
    loc.append(s)
print(min(loc))

loc = []
for start, length in zip(seeds[::2], seeds[1::2]):
    s_ranges = [[start, start+length]]
    for m in maps:
        off_ranges = []
        for off, ms, me in m:
            temp_ranges = []
            for ss, se in s_ranges:
                if se <= ms or me <= ss:
                    temp_ranges.append([ss, se])
                    continue
                if ss < ms:
                    temp_ranges.append([ss, ms])
                    ss = ms
                if se > me:
                    temp_ranges.append([me, se])
                    se = me
                off_ranges.append([ss+off, se+off])
            if not temp_ranges: break
            s_ranges = temp_ranges
        s_ranges = off_ranges + temp_ranges
    loc += s_ranges
print(min(loc)[0])
