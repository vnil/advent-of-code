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
import re
import time
start_time = time.time()

content = open('i', 'r').readlines()
content = [c.strip() for c in content]

G = defaultdict(list)

for row in content:
    left, right = row.split('-')
    G[left].append(right)
    G[right].append(left)


count1 = 0
def dfs1(node, visited):
    global count1
    if node == 'end':
        count1+=1
        return
    if node in visited:
        return
    if not node.isupper():
        visited.add(node)

    for child in G[node]:
        dfs1(child, visited)

    if not node.isupper():
        visited.remove(node)
dfs1('start', set())    
print(count1)

print("--- %s seconds ---" % (time.time() - start_time))