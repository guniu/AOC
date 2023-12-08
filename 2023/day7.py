# ==================================================
# https://adventofcode.com/2023/day/7

file = open("day7.txt").read().splitlines()

T = "0123456789TJQKA"

def get_type(cards):
    ht = []
    while cards:
        ht.append(cards.count(cards[0]))
        cards = [n for n in cards if n != cards[0]]
    return sorted(ht, reverse=True)[:2]

Hands = []
for line in file:
    hand, bid = line.split()
    hand = [T.index(c) for c in hand]
    Hands.append([get_type(hand), hand, int(bid)])

def get_total(hands):
    return sum(hand[2]*r for r, hand in enumerate(sorted(hands), 1))

print(get_total(Hands))

def get_type2(ht, Js):
    if 0 < Js < 5:
        if sum(ht) < 5: ht.append(1)
        ht.remove(Js)
        ht[0] += Js
    return ht

J = T.index('J')
for hand in Hands:
    c = hand[1]
    hand[0] = get_type2(hand[0], c.count(J))
    while J in c: c[c.index(J)] = 1

print(get_total(Hands))
