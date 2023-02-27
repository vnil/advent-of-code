# Take time to read
# Consider different approaches
# +-1 errors?
# Got last item?


from collections import Counter
from collections import defaultdict, deque
from pprint import pprint as pp
from itertools import combinations
from copy import deepcopy

content = open('ex', 'r').readlines()
content = [c.strip() for c in content]

C = {}
P = {}
d = {}
pos = {}
direction = {}
m = 0
for row in content:
    layer, r = map(int, row.split(': '))
    d[layer] = r
    pos[layer] = 0
    direction[layer] = 'D'
    m = max(layer, m)


delay = 0
while True:
    current = - 1 - delay
    damage = 0

    pos_copy = deepcopy(pos)
    direction_copy = deepcopy(direction)
    ok = True
    for i in range(m+1+delay):
        current += 1
        if current in pos_copy:
            range_ = d[current]
            if i-current % (range_*2-2) == 0:  # <---!!
                print(i, current)
                ok = False

        for k in d.keys():
            if direction_copy[k] == 'D':
                if pos_copy[k] < d[k] - 1:
                    pos_copy[k] += 1
                else:
                    pos_copy[k] -= 1
                    direction_copy[k] = 'U'
            else:
                if pos_copy[k] != 0:
                    pos_copy[k] -= 1
                else:
                    pos_copy[k] = 1
                    direction_copy[k] = 'D'
    if ok:
        print(delay, ':::::')
        break
    delay += 1
