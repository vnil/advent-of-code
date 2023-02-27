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
content = open('i', 'r').readlines()
content = [row.strip() for row in content]

d = defaultdict(lambda: defaultdict(str))
water = defaultdict(lambda: defaultdict(int))

max_y, min_y = -math.inf, math.inf

for row in content:
    part1, part2 = row.split(', ')
    base, level = part1.split('=')
    level = int(level)

    start, stop = list(map(int, part2[2:].split('..')))
    for t in range(start, stop + 1):
        if base == 'y':
            min_y = min(min_y, level)
            max_y = max(max_y, level)
            d[level][t] = '#'
        else:
            min_y = min(min_y, t)
            max_y = max(max_y, t)
            d[t][level] = '#'

queue = deque([(min_y, 500)])
ca = 0
stack = []
while queue:
    ca += 1
    if ca % 50000 == 0:
        count = 0
        for row in water.values():
            for c in row.values():
                if c > 0:
                    count += 1
        print(count)
    (r, c) = queue.pop()
    if r < min_y or r > max_y or d[r][c] == '#' or water[r][c] == 2:
        continue
    stack.append((r, c))
    if water[r][c] == 0:
        water[r][c] = 1
    if d[r+1][c] == '#' or water[r+1][c] == 2:
        h_arr = []
        horizontal_queue = deque([(r, c, 'R')])
        visited = set()
        left = right = False
        while horizontal_queue:

            (hr, hc, direction) = horizontal_queue.pop()
            stack.append((hr, hc))
            if (hr, hc) in visited:
                continue
            visited.add((hr, hc))

            if d[hr][hc] == '#':
                if direction == 'L':
                    left = True
                else:
                    right = True
                continue
            water[hr][hc] = 1
            if d[hr+1][hc] == '#' or water[hr+1][hc] == 2:
                h_arr.append((hr, hc))
                horizontal_queue.append((hr, hc-1, 'L'))
                horizontal_queue.append((hr, hc+1, 'R'))
            else:
                queue.append((hr+1, hc))
        if left and right:
            for (sr, sc) in h_arr:
                water[sr][sc] = 2
            # print(stack)
            while stack:
                R, C = stack.pop()
                if water[R][C] == 1:
                    print('RESTART', (r, c))
                    queue.append((R, C))
                    break
            #print('Filled', r)
            # pp(water)
    else:
        queue.append((r+1, c))
# pp(water)
count = 0
for row in water.values():
    for c in row.values():
        if c > 0:
            count += 1
print(count)

count = 0
for row in water.values():
    for c in row.values():
        if c > 1:
            count += 1
print(count)
