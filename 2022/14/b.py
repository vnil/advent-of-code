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
import time
start_time = time.time()

filename = sys.argv[1]

content = open(filename, 'r').readlines()
content = [c.strip() for c in content]

grid = dict()
largest_y = 0

for row in content:
    parts = row.split(' -> ')
    x = 0
    y = 0
    for i, part in enumerate(parts):
        nx, ny = part.split(',')
    
        nx=int(nx)
        ny=int(ny)
        largest_y = max(largest_y, ny)

        if i == 0:
            x = nx
            y = ny
            continue
        if nx == x:
            for iy in range(min(y, ny), max(y, ny) + 1):
                grid[(x, iy)] = '#'
        else:
            for ix in range(min(x, nx), max(x, nx) + 1):
                grid[(ix, y)] = '#'
        x = nx
        y = ny

for wx in range(-1000, 1000):
    grid[(wx, largest_y+2)] = '#'

wall_count = len(grid)


old_len = -1
while len(grid) != old_len:
    old_len = len(grid)
    x = 500
    y = 0
    old_x = -1
    old_y = -1

    while old_x != x and old_y != y:
        old_x = x
        old_y = y

        while (x, y+1) not in grid:
            y+=1
        if (x-1, y+1) not in grid:
            x-=1
            y+=1
        elif (x+1, y+1) not in grid:
            x+=1
            y+=1
        if y == 0:
            grid[(x, y)] = 'o'
            print(len(grid)-wall_count)
            print("--- %s seconds ---" % (time.time() - start_time))
            exit()
    grid[(x, y)] = 'o'

    



