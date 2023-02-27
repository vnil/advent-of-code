

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


#target area: x=217..240, y=-126..-69

minX = 217
maxX = 240
minY = -126
maxY = -69

#minX = 20
#maxX = 30
#minY = -10
#maxY = -5


def is_hit(x, y):
    return minX <= x <= maxX and minY <= y <= maxY


x = 0
y = 0
dx = 0
dy = 0


for i in range(1, 100):
    test_x = 0
    test_dx = i
    while True:
        test_x+=test_dx
        if test_dx > 0:
            test_dx-=1
        elif x < 0:
            test_dx+=1
        if test_dx == 0:
            break
    if test_x >= minX:
        dx = i
        break

found_dx = dx
highest = 0

s = set()

for start_dy in range(-126, 128):
    for start_dx in range(found_dx, found_dx+240):
        dx = start_dx
        dy = start_dy
        hit = False
        x = 0
        y = 0
        old_highest = highest
        while y >= minY:
            x+=dx
            y+=dy
            highest = max(highest, y)
            if dx > 0:
                dx-=1
            elif x < 0:
                dx+=1

            dy-=1
            hit = is_hit(x, y)
            if hit:
                has_hit = True
                s.add((start_dx, start_dy))
                break
        if not hit:
            highest = old_highest
        #if not hit and has_hit:
        #    print(start_dx, start_dy, old_highest)
        #    break
        old_highest = highest
print('part1:', old_highest)
print('part2:', len(s))


    