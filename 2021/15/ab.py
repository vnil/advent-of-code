

# Take time to read
# Consider different approaches
# +-1 errors?
# Got last item?
# What is the diff between states? Pattern?


from collections import Counter
from collections import defaultdict, deque
from pprint import pprint as pp
from itertools import combinations
from copy import deepcopy
import math
import re
from queue import PriorityQueue

content = open('i', 'r').readlines()
content = [[int(x) for x in c.strip()] for c in content]

X = [(-1, 0), (0, 1), (1, 0), (0, -1)]      

def solve(content):
    D = {}
    D[(0, 0)] = 0

    pq = PriorityQueue()
    pq.put((0, (0, 0)))
    visited = set()
    while not pq.empty():
        (dist, (r, c)) = pq.get()
        visited.add((r, c))

        for dr, dc in X:
            ar = r + dr
            ac = c + dc
            if 0<=ar<len(content) and 0<=ac<len(content[0]):
                if (ar, ac) in visited:
                    continue
                distance = content[ar][ac]
                old_cost = D[(ar, ac)] if (ar, ac) in D else math.inf
                new_cost = D[(r, c)] + distance
                if new_cost < old_cost:
                    pq.put((new_cost, (ar, ac)))
                    D[(ar, ac)] = new_cost
        if r == len(content) - 1 and c == len(content[0]) - 1:
            return D[(r, c)]

print('part 1', solve(content))

new = []

for r in content:
    n = []
    for i in range(5):
        n += [((a+i)%10+1) if a+i > 9 else a+i for a in r]
    new.append(n)

cpy_new = deepcopy(new)
new = []
for i in range(5):
    for r in cpy_new:
        new.append([((a+i)%10+1) if a+i > 9 else a+i for a in r])
    
print('part 2', solve(new))