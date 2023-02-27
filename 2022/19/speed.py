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
import sys

filename = "i"

content = open(filename, 'r').readlines()
content = [c.strip() for c in content]
g = set()
for row in content:
    x, y, z = row.split(',')
    x, y, z = int(x), int(y), int(z)
    g.add((x, y, z))

d = [(0, 0, 1),(0, 0, -1), (0, 1, 0),(0, -1, 0),(1, 0, 0),(-1, 0, 0)]


count = 0
closed = set()
def can_escape(p):
    q = deque([p])
    visited = set()
    while q:
        x, y, z = q.popleft()
        if (x, y, z) in visited:
            continue
        visited.add((x, y, z))
        if (x, y, z) in g:
            continue
        if x < 0 or x > 21:
            if y < 0 or y > 21:
                if z < 0 or z > 21:
                    
                    return True
        for dx, dy, dz in d:
            q.append((x+dx, y+dy, z+dz))
    closed.add(p)
    return False
            


for x, y, z in g:
    for dx, dy, dz in d:
        if (dx+x, dy+y, dz+z) not in g:
            if can_escape((dx+x, dy+y, dz+z)):
                count +=1

print(count)

