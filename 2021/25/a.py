

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
grid = [[x for x in c.strip()] for c in content]

R = len(grid)
C = len(grid[0])

count = 0
def pg(g):
    for row in g:
        print(''.join(row))
    print()

moved = True
ca = 0
while moved:
    
    ca+=1
    moved = False
    grid_copy = deepcopy(grid)
    for r in range(R):
        for c in range(C):
            
            if grid[r][c] == '>':
                next_c = (c+1)%C
                if grid[r][next_c] == '.':
                    grid_copy[r][next_c] = '>'
                    grid_copy[r][c] = '.'
                    moved = True
    grid = deepcopy(grid_copy)
    
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'v':
                next_r = (r+1)%R
                if grid[next_r][c] == '.':
                    grid_copy[next_r][c] = 'v'
                    grid_copy[r][c] = '.'
                    moved = True
    grid = deepcopy(grid_copy)

    count+=1

print(count)