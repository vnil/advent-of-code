

# Take time to read
# Consider different approaches
# +-1 errors?
# Got last item?
# What is the diff between states? Pattern?


from collections import Counter
from collections import defaultdict, deque
from pprint import pprint as pp
from itertools import combinations, permutations
from copy import deepcopy
import math
import re
from queue import PriorityQueue
import json

content = open('i', 'r').readlines()
#content = [[int(x) for x in c.strip()] for c in content]
content = [c.strip() for c in content]

#on x=-11829..-1061,y=19988..32790,z=-92294..-55506
#off x=21352..40945,y=40771..48583,z=-67151..-59151

instructions = []

for row in content:
    second = ''
    first = row.split(' ')[0]
    if first == 'on':
        second = row[3:]
    else:
        second = row[4:]
    parts = second.split(',')
    arr = []
    for part in parts:
        cord, ran = part.split('=')
        small, large = [int(a) for a in ran.split('..')]
        if small > large:
            large, small = small, large
        arr.append((small, large))
    instructions.append((first, arr))

grid = defaultdict(int)

for inst in instructions:
    should_on, cords = inst
    #print('::', cords[0][1])
    for x in range(max(-50, cords[0][0]), min(51, cords[0][1] + 1)):
        for y in range(max(-50, cords[1][0]), min(51, cords[1][1] + 1)):
            for z in range(max(-50, cords[2][0]), min(51, cords[2][1] + 1)):
                grid[(x, y, z)] = should_on

print(Counter(grid.values())['on'])        
        

    