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
                connections[a][target] = len(list(reversed(path)))-1 #Reveersed to allow popping instead
                connections[target][a] = len(path)-1

                break
            for potential in g[current]:
                q.append((potential, list(path) + [potential]))


pipes = g.keys()
interesting_pipes = interesting_pipes[1:]

all_paths = []

def paths(node, minutes, path):
    global all_paths
    can_continue = False
    for target in interesting_pipes:
        if target in path:
            continue
        cost = connections[node][target]+1
        if cost >= minutes:
            continue
        can_continue = True
        path.append(target)
        paths(target, minutes - cost, path)
        path.pop()
    if not can_continue:
        all_paths.append(list(path))


def score(path):
    minutes_left = M
    acc = 0
    prev_node = None
    points_map = defaultdict(int)
    for node in path:
        if prev_node:
            minutes_left -= connections[prev_node][node]
        if node != 'AA': # Open valve if not AA
            minutes_left -= 1
            points = rates[node]*max(minutes_left, 0)
            acc += points
            points_map[node] = points
        
        prev_node = node
    return points_map
    

paths('AA', M, ['AA'])

c=0
maps = [score(a) for a in all_paths]

c = 0
best = 0
for i, me in enumerate(maps):
    c+=1
    if c%10 == 0:
        print(c, len(maps))
    for elephant in maps[i+1:]:
        s = 0
        for node in set(me.keys()) | set(elephant.keys()):
            s += max(me[node], elephant[node])
        
        best = max(best, s)

print(best)