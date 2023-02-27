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

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

GRID_SIZE = 50

def teleporter(x, y, try_x, try_y, rotation):
    new_rotation = rotation
    global GRID_SIZE
    from_grid_x = x//GRID_SIZE
    from_grid_y = y//GRID_SIZE

    if from_grid_x < 0 or from_grid_x > 3 or from_grid_y < 0 or from_grid_y > 4:
        print('NOPE!') 
        exit()

    f = (from_grid_x, from_grid_y)

    to_grid_x = try_x//GRID_SIZE
    to_grid_y = try_y//GRID_SIZE

    t = (to_grid_x, to_grid_y)
    print(f, (to_grid_x, to_grid_y))
    if f == (1, 0):
        if t == (0, 0): #check
            try_y = 2*GRID_SIZE+(GRID_SIZE-(y%50)-1)
            try_x = 0
            new_rotation = 0
        elif t == (1, -1): #check
            try_y = 2*GRID_SIZE+x
            try_x = 0
            new_rotation = 0
    elif f == (2, 0):
        if t == (2, -1): #check
            try_y = 4*GRID_SIZE-1
            try_x = x-2*GRID_SIZE
            new_rotation = 3
        elif t == (3, 0): #check
            try_y = 2*GRID_SIZE+(GRID_SIZE-(y%50)-1) # + ?
            try_x = GRID_SIZE*2-1
            new_rotation = 2
        elif t == (2, 1): #check
            try_y = x-GRID_SIZE
            try_x = 2*GRID_SIZE-1
            new_rotation = 2
    elif f == (1, 1):
        if t == (0, 1): #check
            try_y = 2*GRID_SIZE
            try_x = y-GRID_SIZE
            new_rotation = 1
        elif t == (2, 1): #check
            try_y = GRID_SIZE-1
            try_x = y+GRID_SIZE
            new_rotation = 3
    elif f == (1, 2):
        if t == (2, 2): #check
            try_y = (GRID_SIZE-(y%50)-1)
            try_x = GRID_SIZE*3-1
            new_rotation = 2
        elif t == (1, 3): #check
            try_y = x+2*GRID_SIZE
            try_x = GRID_SIZE-1
            new_rotation = 2
    elif f == (0, 2):
        if t == (-1, 2): #checke
            try_y = (GRID_SIZE-(y%50)-1)
            try_x = GRID_SIZE
            new_rotation = 0
        elif t == (0, 1): #check
            try_y = x+GRID_SIZE
            try_x = GRID_SIZE
            new_rotation = 0
    elif f == (0, 3):
        if t == (-1, 3): #check
            try_y = 0
            try_x = y-2*GRID_SIZE
            new_rotation = 1
        elif t == (0, 4): #check
            try_y = 0
            try_x = x+2*GRID_SIZE
            new_rotation = 1
        elif t == (1, 3):
            try_y = GRID_SIZE*3-1
            try_x = y-2*GRID_SIZE
            new_rotation = 3
    print(x, y, rotation)
    print(try_x, try_y, new_rotation)
    print('----')

    if m[try_y][try_x] == '#':
        return False, (x, y), rotation
    else:
        if m[try_y][try_x] != '.':
            print("WHAA?")
            exit()
        return True, (try_x, try_y), new_rotation
io = 0

for steps, rot in arr:
    # move steps, then rotate rot
    for _ in range(steps):
        x, y = current_pos
        print((x, y), current_rotation)
        tx, ty = x+d[current_rotation][0], y+d[current_rotation][1]
        if 0 <= tx < len(m[0]) and 0 <= ty < len(m) and m[ty][tx] != ' ':
            if m[ty][tx] == '.':
                current_pos = (tx, ty)
            elif m[ty][tx] == '#':
                break
            else:
                assert False
        # Empty, wrap around
        else:
            io+=1
            ok, new_cord, new_rotation = teleporter(x, y, tx, ty, current_rotation)
            print(ok)
            if ok:
                #if io > 20: exit()
                current_pos = new_cord
                current_rotation = new_rotation
            else:
                #if io > 20: exit()
                break


    #rotate
    if rot == 'R':
        current_rotation = (current_rotation+1)%4
    else:
        current_rotation = (current_rotation+3)%4
current_rotation = (current_rotation+3)%4
                    
row = current_pos[1]+1
col = current_pos[0]+1
print(row*1000+4*col+current_rotation)