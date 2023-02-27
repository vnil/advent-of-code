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
import time
start_time = time.time()

filename = sys.argv[1]

content = open(filename, 'r').readlines()
content = [c.strip() for c in content]
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

g=set()
max_x = 0
min_x = 0
max_y = 0
min_y = 0
max_z = 0
min_z = 0


for row in content:
    x, y, z = list(map(int, [x for x in row.split(',')]))
    max_x = max(x, max_x)
    min_x = min(x, min_x)
    max_y = max(y, max_y)
    min_y = min(y, min_y)
    max_z = max(z, max_z)
    min_z = min(z, min_z)

    g.add((x, y, z))

max_x+=1
min_x-=1
max_y+=1
min_y-=1
max_z+=1
min_z-=1

d = [(1, 0, 0),(-1, 0, 0), (0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0)]
stuck = set()
free = set()

def trapped(x, y, z):
    global stuck, free
    visited = set()
    q = deque([(x, y, z)])
    while q:
        tx, ty, tz = q.popleft()
        if (tx, ty, tz) in visited:
            continue
        visited.add((tx, ty, tz))
        if (tx, ty, tz) in g:
            continue
        if (tx, ty, tz) in stuck:
            return True
        if (tx, ty, tz) in free:
            return False

        if tx == min_x or tx == max_x:
            if ty == min_y or ty == max_y:
                if tz == min_z or tz == max_z:
                    stuck = visited | stuck   
                    return False
        
        for dx, dy, dz in d:
            q.append((tx+dx, ty+dy, tz+dz))
    free = visited | free
    return True

tot = 0
for x, y, z in g:
    visible_sides = 0
    for dx, dy, dz in d:
        tx = x + dx
        ty = y + dy
        tz = z + dz
        if (tx, ty, tz) not in g and not trapped(tx, ty, tz):
            visible_sides+=1
    tot+=visible_sides

print(tot)