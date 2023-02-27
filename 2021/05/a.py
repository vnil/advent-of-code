# Take time to read
# Consider different approaches
# +-1 errors?
# Got last item?


from collections import Counter
from collections import defaultdict, deque
from pprint import pprint as pp
from itertools import combinations
from copy import deepcopy
import math
import re

content = open('i', 'r').readlines()
content = [c.strip() for c in content]

arr = []

for row in content:
    part1, part2 = row.split(' -> ')

    x1, y1 = [int(x) for x in part1.split(',')]
    x2, y2 = [int(x) for x in part2.split(',')]
    if x1 == x2 or y1 == y2:
        arr.append((x1, y1, x2, y2))

d = defaultdict(lambda: defaultdict((int)))
for item in arr:
    x1, y1, x2, y2 = item

    if x1 == x2:
        if x1 > x2:
            x2, x1 = x1, x2
        if y1 > y2:
            y2, y1 = y1, y2
        for y in range(y1, y2+1):
            d[y][x1] += 1
    elif y1 == y2:
        if x1 > x2:
            x2, x1 = x1, x2
        if y1 > y2:
            y2, y1 = y1, y2
        for x in range(x1, x2+1):
            d[y1][x] += 1

cn = 0
for r in d:
    for c in d[r]:
        if d[r][c] > 1:
            cn += 1
print(cn)
