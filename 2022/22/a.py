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

content = open(filename, 'r').read()
parts = content.split('\n\n')
#content = [c.strip() for c in content]

instructions = parts[1].strip()

map_raw = parts[0]


m = map_raw.split('\n')

start_pos = (m[0].find('.'), 0)

arr = []

current = ""
for ins in instructions:
    if ins.isupper():
        arr.append((int(current), ins))
        current = ""
    else:
        current += ins

current_rotation = 0
current_pos = start_pos
print(arr)

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

GRID_SIZE = 50

def teleporter(x, y, try_x, try_y, rotation):
    global GRID_SIZE
    from_grid_x = x//GRID_SIZE
    from_grid_y = y//GRID_SIZE

    to_grid_x = try_x//GRID_SIZE
    to_grid_y = try_y//GRID_SIZE
    print(from_grid_x, from_grid_y, to_grid_x, to_grid_y)

    # try_x, try_y = tx, ty
    #     if current_rotation == 0:
    #         try_x = 0
    #     elif current_rotation == 1:
    #         try_y = 0
    #     elif current_rotation == 2:
    #         try_x = len(m[0]) - 1
    #     else:
    #         try_y = len(m) - 1
    #     ok = True
    #     while True:
    #         if m[try_y][try_x] == '.':
    #             break
    #         elif m[try_y][try_x] == '#':
    #             ok = False
    #             break
    #         try_x += d[current_rotation][0]
    #         try_y += d[current_rotation][1]
    #     if ok:
    #         current_pos = (try_x, try_y)
    #     else:
    #         break

for steps, rot in arr:
    # move steps, then rotate rot
    print('CURRENT:', current_pos, current_rotation)
    for _ in range(steps):
        x, y = current_pos
        tx, ty = x+d[current_rotation][0], y+d[current_rotation][1]
        if 0 <= tx < len(m[0]) and 0 <= ty < len(m) and m[ty][tx] != ' ':
            if m[ty][tx] == '.':
                current_pos = (tx, ty)
            elif m[ty][tx] == '#':
                break
        # Empty, wrap around
        else:
            teleport(x, y, tx, ty, current_rotation)

    #rotate
    if rot == 'R':
        current_rotation = (current_rotation+1)%4
    else:
        current_rotation = (current_rotation+3)%4
current_rotation = (current_rotation+3)%4
print(current_pos)
                    
row = current_pos[1]+1
col = current_pos[0]+1
print(row*1000+4*col+current_rotation)