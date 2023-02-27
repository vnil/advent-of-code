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


rev = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

p = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

p2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}
points=0
points2=[]
for row in content:
    stack = []
    ok = True
    for c in row:
        if c == '(':
            stack.append('(')
        elif c == '[':
            stack.append('[')
        elif c == '{':
            stack.append('{')
        elif c == '<':
            stack.append('<')
        else:
            # closing
            should_be = rev[stack.pop()]
            if c != should_be:
                points+=p[c]
                ok = False
                break
    if ok:
        local_score = 0
        while stack:
            missing_last = rev[stack.pop()]
            local_score *= 5
            local_score += p2[missing_last]
        points2.append(local_score)

print('part1', points)
points2.sort()
print('part2', points2[len(points2)//2])
