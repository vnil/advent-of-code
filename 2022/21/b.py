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

org = dict(g)
while len(g.keys()):
    cpy = dict(g)
    for monkey in cpy.keys():
        if g[monkey][0] in vals and g[monkey][1] in vals:
            if monkey == 'root':
                print(g[monkey][0], g[monkey][1], str(vals[g[monkey][0]]) + g[monkey][2] + str(vals[g[monkey][1]]))
            vals[monkey] = eval(str(vals[g[monkey][0]]) + g[monkey][2] + str(vals[g[monkey][1]]))
            del g[monkey]
g = org
target_val = vals[g['root'][1]] # Höger värde för både input och exempel
print('TARGET VAL', target_val)

real_path = None
q = deque([('root', [])])
seen = set()
while q:
    item, path = q.popleft()
    if item == 'humn':
        real_path = path
        break
    if item in seen or item not in g:
        continue
    
    seen.add(item)

    cpy = path + [item]
    q.append((g[item][0], cpy))
    q.append((g[item][1], cpy))


real_path+=['humn']
real_path=real_path[1:]
for i,item in enumerate(real_path):
    if item == 'humn':
        print(int(target_val))
        break
    options = g[item]
    compare_to = options[0] if options[0] != real_path[i+1] else options[1]
    lookup = options[1] if options[0] != real_path[i+1] else options[0]
    compare_val = vals[compare_to]
    if g[item][2] == '+':
        target_val-=compare_val
    if g[item][2] == '/':
        if lookup == options[0]:
            target_val*=compare_val
        else:
            target_val/=compare_val

    if g[item][2] == '*':
        target_val/=compare_val

    if g[item][2] == '-':
        if lookup == options[0]:
            target_val+=compare_val
        else:
            target_val=-target_val+compare_val



