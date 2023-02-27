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


ranges = []

GO = 4000000

for row in content:
    parts = row.split()
    sx = int(parts[2][2:-1])
    sy = int(parts[3][2:-1])
    bx = int(parts[8][2:-1])
    by = int(parts[9][2:])
    
    sensors.append((sx, sy))
    beacons.add((bx, by))
    print("ROW")

    distance = abs(sx - bx) + abs(sy - by)

    for target_y in range(GO):
        ranges.append([])
        if abs(sy-target_y) > distance:
            continue
        #within reach
        #smallest
        shortest_x = sx
        largest_x_distance = distance - abs(target_y - sy)
        min_x = shortest_x - largest_x_distance
        max_x = shortest_x + largest_x_distance
        
        #print(ranges, target_y)
        ranges[target_y].append((min_x, max_x))
print("Semi done")
for Y in range(GO):
    a = sorted(ranges[Y], key=lambda x: x[0])

    min_x = max(0, a[0][0])
    max_x = min(GO, a[0][1])

    length = 0
    for item in a[1:]:
        #print(min_x, max_x, length)
        if item[0] <= max_x:
            max_x = min(GO, max(max_x, item[1]))
        else:
            length += max_x - min_x
            min_x = max(0, item[0])
            max_x = min(GO, item[1])
            
    length += max_x - min_x
    if length < GO:
        print(Y, length, a)
        #Manually find the one from the printed range in "a"
print("DONE")
    






    
