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
import functools

filename = sys.argv[1]

content = open(filename, 'r').readlines()
content = [c.strip() for c in content]
g = dict()
rates = dict()

for row in content:
    parts = row.split()
    name = parts[1]
    rate = parts[4][5:-1]
    k = row.split('valve')
    rest = k[1][1:].strip().split(',')
    connections = [a.strip() for a in rest]
    g[name] = connections
    rates[name] = int(rate)

pipes = g.keys()

visited = set()
openable_pipes = len([a for a in pipes if rates[a] > 0])
largest = 0

M = 26
opened = set()


mem = defaultdict(lambda: 999999)

some = defaultdict(lambda: (9999, 0))

# key current pipe, time left
def go(name, minute, pressure, acc):
    global largest, opened
    opened_key = ''.join(sorted(opened))
    mem_key = (name, minute, acc, opened_key)
    if mem[mem_key] <= minute:
        return
    mem[mem_key] = minute
    if some[name][0] < minute and some[name][1] >= pressure:
        return 
    some[name] = (minute, pressure)

    if minute == M:
        #print("arrived")
        largest = max(largest, acc+pressure)
        return
        
    if name not in opened and rates[name] != 0:
        opened.add(name)
        go(name, minute+1, pressure+rates[name], acc+pressure)
        opened.remove(name)
    
    #if len(opened) == openable_pipes:
    #    qw = acc+pressure*(M-minute+1)
    #    if qw > largest:
    #        largest = qw
    #        print(qw, '<----')
    #    return

    for pipe in g[name]:
        go(pipe, minute+1, pressure, acc+pressure)


go('AA', 1, 0, 0)
print(largest)
