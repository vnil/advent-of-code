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


def pri(g):
    for row in g:
        print(''.join(row))
    print('---')


grid = []
for row in content:
    grid.append([])
    for x in row:
        grid[-1].append(x)
pri(grid)

for i in range(100):
    g = deepcopy(grid)
    for y, row in enumerate(g):
        for x, col in enumerate(row):
            grid[0][0] = '#'
            grid[0][len(g[0])-1] = '#'
            grid[len(g)-1][0] = '#'
            grid[len(g)-1][len(g[0])-1] = '#'
            lights_on = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == dy == 0:
                        continue
                    check_y = y + dy
                    check_x = x + dx
                    if 0 > check_y or check_y >= len(grid) or 0 > check_x or check_x >= len(grid[0]):
                        continue
                    if grid[check_y][check_x] == '#':
                        lights_on += 1
            if grid[y][x] == '#':
                if lights_on != 2 and lights_on != 3:
                    g[y][x] = '.'
            else:
                if lights_on == 3:
                    g[y][x] = '#'
            g[0][0] = '#'
            g[0][len(g[0])-1] = '#'
            g[len(g)-1][0] = '#'
            g[len(g)-1][len(g[0])-1] = '#'
    grid = g
    # pri(g)

c = 0
for i in range(len(grid)):
    for k in grid[i]:
        if k == '#':
            c += 1
print(c)
