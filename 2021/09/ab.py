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
content = [[int(x) for x in c.strip()] for c in content]

D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
t = 0

low_points = []
for y in range(len(content)):
    for x in range(len(content[0])):
        ok = True

        for d in D:
            dx, dy = d
            ax = x + dx
            ay = y + dy
            if 0 <= ay < len(content) and 0 <= ax < len(content[0]):
                if content[ay][ax] <= content[y][x]:
                    ok = False
        if ok:
            t+=1+content[y][x]
            low_points.append((y, x))
print('part1', t)

def validate(qy, qx, p, v):
    if content[qy][qx] == 9:
        return False
    one_smaller = False
    for d in D:
        dx, dy = d
        ax = x + dx
        ay = y + dy
        if 0 <= ay < len(content) and 0 <= ax < len(content[0]):
            if content[ay][ax] < content[y][x]:
                if (ay, ax) not in v:
                    return False
    return True

s = []
for p in low_points:
    queue = deque([p])
    visited = set()
    points = 0
    while queue:
        (y, x) = queue.popleft()
        if (y, x) in visited:
            continue
        valid = validate(y, x, p, visited)
        if not valid:
            continue 
        visited.add((y, x))
        points+=1
        for d in D:
            dx, dy = d
            ax = x + dx
            ay = y + dy
            if 0 <= ay < len(content) and 0 <= ax < len(content[0]):                  
                queue.append((ay, ax))
    s.append(points)
s.sort()
s = list(reversed(s))
a = s[0:3]
res = 1
for q in a:
    res*=q
print('part2', res)