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

M = 3
# key current pipe, time left
def go(name, current_minutes, pressure, acc, opened):
    global largest, max_p
    if current_minutes > M:
        return
    print(current_minutes, pressure, acc)

    
    #opened_key = ''.join(sorted(list(opened)))
    #if (name, current_minutes, acc, opened_key) in visited:
    #    return
    #visited.add((name, current_minutes, acc, opened_key))

    if current_minutes >= M:
        print(acc)
        largest = max(largest, acc)
        #print(pressure, current_minutes, opened, largest)
        return

    #just waiting
    if len(opened) == openable_pipes:
        print("baj")
        largest = max(acc+pressure*(M-current_minutes), largest)
        return

    for pipe in g[name]:

        go(pipe, current_minutes+1, pressure, acc+pressure, opened)
        if pipe in opened:
            continue
        if rates[pipe] == 0:
            continue

        
        #if local_cm >= 30:
        #    largest = max(largest, local_acc)
        #    continue
        
        opened.add(pipe)

        
        go(pipe, current_minutes+2, pressure+rates[pipe], acc+pressure*2, opened)
        opened.remove(pipe)


for pipe in pipes:        
    go(pipe, 1, 0, 0, set())
print(largest)


    


def loop_check(pipe, end, path, visited):
    if pipe == end and len(path) > 2:
        print(path)
        return
    if pipe in visited:
        return
    visited.add(pipe)
    
    for t in g[pipe]:
        if rates[t] == 0:
            path.append(t)
            loop_check(t, end, path, visited)
            path.pop()

for pipe in pipes:
    if rates[pipe] != 0:
        continue

    loop_check(pipe, pipe, [], set())




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
