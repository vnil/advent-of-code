# Take time to read
# Consider different approaches
# +-1 errors?
# Got last item?

# 11.33
# 13.26
# 13.56
from collections import Counter
from collections import defaultdict, deque
from pprint import pprint as pp
from itertools import combinations
from copy import deepcopy
import math

test_cases = []

reg = [0, 0, 0, 0]

content = open('i', 'r').readlines()
content = [row.strip() for row in content]
current = []
for i, row in enumerate(content):
    if len(row) < 2:
        test_cases.append(current)
        current = []
        continue

    if ':' in row:
        _, part2 = row.split(': ')
        row = part2
        nrs = [int(x) for x in row[1:-1].split(', ')]
        current.append(nrs)
    else:
        nrs = [int(x) for x in row.split(' ')]
        current.append(nrs)
if len(current) > 0:
    test_cases.append(current)


def addr(a, b, c):
    reg[c] = reg[a] + reg[b]


def addi(a, b, c):
    reg[c] = reg[a] + b


def mulr(a, b, c):
    reg[c] = reg[a] * reg[b]


def muli(a, b, c):
    reg[c] = reg[a] * b


def banr(a, b, c):
    reg[c] = reg[a] & reg[b]


def bani(a, b, c):
    reg[c] = reg[a] & b


def borr(a, b, c):
    reg[c] = reg[a] | reg[b]


def bori(a, b, c):
    reg[c] = reg[a] | b


def setr(a, b, c):
    reg[c] = reg[a]


def seti(a, b, c):
    reg[c] = a


def gtir(a, b, c):
    reg[c] = 1 if a > reg[b] else 0


def gtri(a, b, c):
    reg[c] = 1 if reg[a] > b else 0


def gtrr(a, b, c):
    reg[c] = 1 if reg[a] > reg[b] else 0


def eqir(a, b, c):
    reg[c] = 1 if a == reg[b] else 0


def eqri(a, b, c):
    reg[c] = 1 if reg[a] == b else 0


def eqrr(a, b, c):
    reg[c] = 1 if reg[a] == reg[b] else 0


arr = [addr,
       addi,
       mulr,
       muli,
       banr,
       bani,
       borr,
       bori,
       setr,
       seti,
       gtir,
       gtri,
       gtrr,
       eqir,
       eqri,
       eqrr]

c = 0

d = {}

for test in test_cases:
    cc = 0
    for f in arr:
        reg = [x for x in test[0]]
        f(*test[1][1:])
        if reg == test[2]:
            cc += 1
            if f.__name__ not in d:
                d[f.__name__] = set()
            d[f.__name__].add(test[1][0])
    if cc >= 3:
        c += 1


m = {}
c = 0
while c < 20:
    c += 1
    cpy = deepcopy(d)
    for k in cpy:
        if len(d[k]) == 1:
            val = list(d[k])[0]
            for k2 in cpy:
                if k2 in d and val in d[k2]:
                    d[k2].remove(val)
                    if len(d[k2]) == 0:
                        del d[k2]
            m[val] = k

inst = open('i2', 'r').readlines()
inst = [row.strip() for row in inst]


reg = [0, 0, 0, 0]
for s in inst:
    a, b, c, d = list(map(int, s.split(' ')))

    locals()[m[a]](b, c, d)
print(reg)
