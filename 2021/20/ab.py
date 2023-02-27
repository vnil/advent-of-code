

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
import json

content = open('i', 'r').readlines()
content = [c.strip() for c in content]

enchance = content[0]

grid = content[2:]

org_grid = deepcopy(grid)

def pr(g):
    s = ''
    count = 0
    for r in g:
        s+=''
        for c in r:
            s+=c
            if c == '#':
                count+=1
        s = ''
    return count

def pad_grid(g):
    pad = 8
    new_grid = []
    top = ['.' for _ in range(len(g) + pad*2)]
    for _ in range(pad):
        new_grid.append(list(top))

    for r in g:
        r = list(r)
        new_grid.append(list('.' * pad + ''.join(r) + '.' * pad))

    for _ in range(pad):
        new_grid.append(list(top))
    return new_grid

def strip_grid(g):
    strip = 9
    new_grid = []
    
    for i,r in enumerate(g):
        if i > strip and i <= len(g) - strip:
            r = list(r)
            new_grid.append(r[strip:len(g) - strip])

    return new_grid

def solve(grid, count):
    for it in range(count):
        grid = pad_grid(grid)
        grid_copy = deepcopy(grid)

        R = len(grid)
        C = len(grid[0])

        for r in range(R):
            for c in range(C):
                sub = ''
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        ar = r + dr
                        ac = c + dc
                        if 0 <= ar < R and 0 <= ac < C:
                            sub += grid[ar][ac]
                        else:
                            sub += '.'
                        
                if len(sub) != 9:
                    continue
                
                nr = int(sub.replace('#', '1').replace('.', '0'), 2)
                char = enchance[nr]

                grid_copy[r][c] = char

        grid = grid_copy
        if it % 2 == 1:
            grid = strip_grid(grid)


    return pr(grid)

print('part1', solve(org_grid, 2))
print('part2', solve(org_grid, 50))


