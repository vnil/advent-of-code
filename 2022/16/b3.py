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
import random



filename = sys.argv[1]

content = open(filename, 'r').readlines()
content = [c.strip() for c in content]
g = dict()
rates = dict()
interesting_pipes = ['AA']
M = int(sys.argv[2]) 

# Parsing
for row in content:
    parts = row.split()
    name = parts[1]
    rate = parts[4][5:-1]
    k = row.split('valve')
    rest = k[1][1:].strip().split(',')
    connections = [a.strip() for a in rest]
    g[name] = connections
    rates[name] = int(rate)
    if int(rate) > 0:
        print(name)
        interesting_pipes.append(name)

connections = defaultdict(dict)
max_pressure = sum(rates.values())

# Extract shortest paths
for i, a in enumerate(interesting_pipes):
    for b in interesting_pipes[i:]:
        if a == b:
            continue
        q = deque([(a, [a])])
        target = b
        visited = set()
        while q:
            current, path = q.popleft()
            if current in visited:
                continue
            visited.add(current)
            if current == target:
                connections[a][target] = len(path)-1
                connections[target][a] = len(path)-1

                break
            for potential in g[current]:
                q.append((potential, list(path) + [potential]))


pipes = g.keys()
interesting_pipes = interesting_pipes[1:]
nr_of_interesting_pipes = len(interesting_pipes)
#pp(interesting_pipes)
#pp(connections)

opened = set()

total_acc = 0

visited = dict()

open_cache = set()

def solve(pipe, minutes, acc, debug):
    global total_acc, opened, visited
    #print(debug)

    opened_key = ''.join(sorted(opened))
    #key = (pipe, minutes, total_acc)
    #if key in visited and visited[key] > total_acc:
        #print("hit")
        #return
        
    #visited[key] = total_acc
    #ADCBJEHEC
    if minutes > M or len(opened) == nr_of_interesting_pipes:
        if total_acc < acc:
            print("NEW:", acc)
            total_acc = acc
            ok = True
            d="ADCBJE" #"ADCBJEHEC"
            for i, a in enumerate(debug[0:len(d)]):
                if a[0][0] != d[i]:
                    ok = False
                    break
            if ok:
                print(debug)            
            
        return
    for target in interesting_pipes:
        if target == pipe:
            continue
        if pipe not in opened:
            opened.add(pipe)
            open_cache.add(pipe+":"+str(minutes))
            new_acc=acc+rates[pipe]*max(0, (M-minutes-1))
            solve(target, minutes+connections[pipe][target] + 1, new_acc, list(debug) + [(pipe, new_acc, 'A', str(opened), minutes)])
            opened.remove(pipe)
            open_cache.remove(pipe+":"+str(minutes))
        
        solve(target, minutes+connections[pipe][target], acc, list(debug) + [(pipe, acc, str(opened), minutes)])
    

for pipe in connections['AA'].keys():
    solve(pipe, connections['AA'][pipe], 0, [('AA', 0)])

print(total_acc)