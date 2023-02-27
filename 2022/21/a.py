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

g = dict()
vals = dict()

for row in content:
    parts = row.split(': ')
    id_ = parts[0]
    if len(parts[1].split()) == 1:
        vals[id_] = int(parts[1])
    else:
        deps = [parts[1][0:4], parts[1][7:], parts[1][5:6]]
        g[id_] = deps

#pp(g)
pp(vals)

while len(g.keys()):
    cpy = dict(g)
    for monkey in cpy.keys():
        if g[monkey][0] in vals and g[monkey][1] in vals:
            if monkey == 'roow':
                print(g[monkey][0], g[monkey][1])
            vals[monkey] = eval(str(vals[g[monkey][0]]) + g[monkey][2] + str(vals[g[monkey][1]]))
            del g[monkey]

#pp(vals)
print(vals['root'])

