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

sensors = []
beacons = set()

target_y = 2000000

ranges = []

for row in content:
    parts = row.split()
    sx = int(parts[2][2:-1])
    sy = int(parts[3][2:-1])
    bx = int(parts[8][2:-1])
    by = int(parts[9][2:])
    
    sensors.append((sx, sy))
    beacons.add((bx, by))

    distance = abs(sx - bx) + abs(sy - by)
    
    if abs(sy-target_y) > distance:
        continue
    #within reach
    #smallest
    shortest_x = sx
    largest_x_distance = distance - abs(target_y - sy)
    min_x = shortest_x - largest_x_distance
    max_x = shortest_x + largest_x_distance

    ranges.append((min_x, max_x))

a = sorted(ranges, key=lambda x: x[0])

min_x = a[0][0]
max_x = a[0][1]

length = 0

for item in a[1:]:
    print(min_x, max_x, length)
    if item[0] <= max_x:
        max_x = max(max_x, item[1])
    else:
        length += max_x - min_x
        min_x = item[0]
        max_x = item[1]
        
length += max_x - min_x

print(length)
    






    
