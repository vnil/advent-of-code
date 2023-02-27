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

filename = sys.argv[1]

content = open(filename, 'r').readlines()
content = [c.strip() for c in content]

D = [(0, 1), (1, 0), (0, -1), (-1, 0)]


goal = None

q = deque()

for r in range(len(content)):
    for c in range(len(content[0])):
        if content[r][c] == 'S':
            content[r] = content[r].replace('S', 'a')
            q.append(((c, r), 'a', 0, []))
        elif content[r][c] == 'E':
            content[r] = content[r].replace('E', 'z')
            goal = (c, r)
        elif content[r][c] == 'a':
            q.append(((c, r), 'a', 0, []))






seen = set()


while q:
    item, height, steps, debug = q.popleft()
    x, y = item
    
    if item in seen:
        continue
    seen.add(item)
    if (x, y) == goal:
        print(steps) # Maybe off by one
        continue
    for dx, dy in D:
        nx = x+dx
        ny = y+dy
        if 0 <= ny < len(content) and 0 <= nx < len(content[0]):
            if ord(content[ny][nx]) - 1 <= ord(content[y][x]):
                q.append(((nx, ny), content[y][x], steps+1, list(debug)+[(nx, ny)]))
print('DOne')
    