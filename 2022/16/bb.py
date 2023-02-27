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
interesting_pipes = []

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

pipes = g.keys()

used = set()

max_pressure = sum(rates.values())

connections = defaultdict(dict)

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
                connections[a][target] = path
                connections[target][a] = list(reversed(path))
                for ui in path:
                    used.add(ui)
                break
            for potential in g[current]:
                q.append((potential, list(path) + [potential]))



print(len(used))