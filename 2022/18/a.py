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

filename = sys.argv[1]

content = open(filename, 'r').readlines()
content = [c.strip() for c in content]

g=set()

for row in content:
    x, y, z = list(map(int, [x for x in row.split(',')]))
    g.add((x, y, z))


d = [(1, 0, 0),(-1, 0, 0), (0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0)]
tot = 0

for x, y, z in g:
    visible_sides = 0
    
    for dx, dy, dz in d:
        tx = x + dx
        ty = y + dy
        tz = z + dz
        if (tx, ty, tz) not in g:
            visible_sides+=1

    tot+=visible_sides




    