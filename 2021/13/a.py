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

content = open('i', 'r').readlines()
content = [c.strip() for c in content]

G = defaultdict(list)

folds = []

paper = defaultdict(lambda: defaultdict(bool))

maxY = 0
maxX = 0

for row in content:
    if ',' in row:
        x, y = list(map(int, row.split(',')))
        paper[y][x] = True
        maxY = max(maxY, y)
        maxX = max(maxX, x)
    elif '=' in row:
        left, right = row.split('=')
        cord = int(right)
        ax = left[-1:]
        folds.append((ax, cord))
folds = folds[0:1]
for ax, cord in folds:
    if ax == 'y':
        for y in range(cord, maxY+1):
            for x in range(maxX+1):
                if paper[y][x]:
                    new_y = cord-(y-cord)
                    paper[new_y][x] = True
                    paper[y][x] = False
    else:
        for y in range(maxY+1):
            for x in range(cord, maxX+1):
                if paper[y][x]:
                    new_x = cord-(x-cord)
                    paper[y][new_x] = True
                    paper[y][x] = False
count = 0
for y in paper:
    for x in paper:
        if paper[y][x]:
            count+=1

print(count)


