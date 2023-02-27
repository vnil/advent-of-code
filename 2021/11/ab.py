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
content = [[int(a) for a in c.strip()] for c in content]

count = 0

def flash(r, c, flashed):
    global count
    if (r, c) in flashed:
        return
    flashed.add((r, c))
    
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            rr = r + dr
            cc = c + dc
            if 0 <= rr < len(content) and 0 <= cc < len(content[0]):
                if dr == 0 and dc == 0:
                    continue
                content[rr][cc]+=1
                if content[rr][cc] > 9:
                    flash(rr, cc, flashed)


for i in range(100000000):
    flashed = set()
    for r, row in enumerate(content):
        for c, energy in enumerate(row):
            content[r][c] +=1
    for r, row in enumerate(content):
        for c, energy in enumerate(row):
            if content[r][c] > 9:
                flash(r, c, flashed)
    part2 = True
    for r, row in enumerate(content):
        for c, energy in enumerate(row):
            if content[r][c] > 9:
                content[r][c] = 0
                count+=1
            else:
                part2 = False
    if part2:
        break
    if i == 99:
        print('part1', count)
print('part2', i+1)
