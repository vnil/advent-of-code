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

count2 = 0
arr = []
def dfs2(node, V):
    global count2
    
    if node == 'end':
        count2+=1
        return
    if node in V:
        if (node == 'start' or node == 'end') and V[node] == 1:
            return
        has_one = False
        for val in V:
            if V[val] == 2:
                has_one = True
                break
        if has_one and V[node] > 0:
            return
    if not node.isupper():
        V[node]+=1

    for child in G[node]:
        dfs2(child, V)

    if not node.isupper():
        V[node]-=1
dfs2('start', defaultdict(int))
print(count2)

print("--- %s seconds ---" % (time.time() - start_time))