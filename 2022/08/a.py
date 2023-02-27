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
content = [c.strip() for c in content]

width = len(content[0])
height = len(content)

S = set()

d = dict()

for i in range(height):
    for x in range(width):
        d[(x, i)] = 1

for i, row in enumerate(content):
    left = 0
    right = width - 1
    max_left = -1
    max_right = -1

    while left < width:
        if max_left < int(content[i][left]):
            S.add((left, i))
            d[(left, i)] *= max(1, left)
        max_left = max(max_left, int(content[i][left]))
        left += 1
    while right > 0:
        if max_right < int(content[i][right]):
            S.add((right, i))
            d[(right, i)] *= max(1, right - width - 1)
        max_right = max(max_right, int(content[i][right]))
        
        right -= 1
    
for i in range(width):
    top = 0
    bottom = height - 1
    max_top = -1
    max_bottom = -1
    
    while top < height:
        if max_top < int(content[top][i]):
            S.add((i, top))
            d[(i, top)] *= max(1, top)
        max_top = max(max_top, int(content[top][i]))
        top += 1
    while bottom > 0:
        if max_bottom < int(content[bottom][i]):
            S.add((i, bottom))
            d[(i, bottom)] *= max(1, bottom - height - 1)
        max_bottom = max(max_bottom, int(content[bottom][i]))
        bottom -= 1
print(len(S))

o = 0

m = 0

for x, y in S:
    d = 1
    score = 1
    while x-d >= 0 and content[y][x-d] < content[y][x]:
        d+=1
    score *= d if x-d >= 0 else d - 1

    d = 1
    while x+d < width and content[y][x+d] < content[y][x]:
        d+=1
    score *= d if x+d < width else d - 1

    d = 1
    while y-d >= 0 and content[y-d][x] < content[y][x]:
        d+=1
    score *= d if y-d >= 0 else d - 1


    d = 1
    while y+d < height and content[y+d][x] < content[y][x]:
        d+=1
    score *= d if y+d < height else d - 1
    m = max(m, score)

    
print(m)

