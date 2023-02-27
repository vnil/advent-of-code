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

stacks = []

for i, row in enumerate(content):
    if row[1] == '1':
        break
    a = 1
    stack_index = 0
    while a < len(row):
        if len(stacks)<=stack_index:
            stacks.append(deque([]))

        if len(row)>a and row[a] != " ":
            stacks[stack_index].appendleft(row[a])
        a+=4
        stack_index += 1


for row in content:
    if len(row) == 0 or row[0] != 'm':
        continue
    
    _, count, _, from_stack, _, to_stack = row.split(" ")
    count = int(count)
    from_stack = int(from_stack) - 1
    to_stack = int(to_stack) - 1
    
    ne = deque([])
    for i in range(count):
        ne.append(stacks[from_stack].pop())

    for a in reversed(ne):    
        stacks[to_stack].append(a)

print(''.join([k[-1] for k in stacks]))
