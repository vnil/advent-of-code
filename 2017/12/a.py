# Take time to read
# Consider different approaches
# +-1 errors?
# Got last item?


from collections import Counter
from collections import defaultdict, deque
from pprint import pprint as pp
from itertools import combinations
from copy import deepcopy

content = open('input', 'r').readlines()
content = [c.strip() for c in content]

C = {}
P = {}

for row in content:
    left, right = row.split(' <-> ')
    right = list(map(int, right.split(', ')))
    left = int(left)
    C[left] = right
    for c in right:
        P[c] = right

s = set()

p2 = 0
for k in range(2000):
    if k in s:
        continue
    q = deque([k])
    while q:
        item = q.popleft()
        if item in s:
            continue
        s.add(item)
        for c in C[item]:
            q.append(c)
        for c in P[item]:
            q.append(c)
    p2 += 1

print(len(s), p2)
