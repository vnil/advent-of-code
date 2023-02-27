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

d = {
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0),
    '^': (0, -1)
}

dirs = d.keys()

deltas = d.values()

bliz = []

content = open(filename, 'r').readlines()
content = [c.strip() for c in content]
for r, row in enumerate(content):
    for c, char in enumerate(row):
        if char in dirs:
            bliz.append(((c, r), char))

start_pos = (1, 0)

end_pos = None
for c, char in enumerate(content[-1]):
    if char == '.':
        end_pos = (c, len(content) -1 )


deq = deque([(start_pos, 0)])
visited = set()


calculated_states = dict()

def get_state(steps):
    if steps in calculated_states:
        return calculated_states[steps]
    m = deepcopy(content)
    current = bliz
    for _ in range(steps):
        new_bliz = []
        for ar in current:
            (sx, sy), char = ar
            dx, dy = d[char]
            tx = dx+sx
            ty = dy+sy

            if tx == 0:
                tx = len(content[0])-2
            elif tx == len(content[0])-1:
                tx = 1
            elif ty == 0:
                ty = len(content)-2
            elif ty == len(content)-1:
                ty = 1
            new_bliz.append(((tx, ty), char))
        current = new_bliz
        
    storm_set = set()
    for pos, _ in current:
        storm_set.add(pos)

    calculated_states[steps] = storm_set
    return storm_set
    



while deq:
    ((x, y), steps) = deq.popleft()
    #if steps > 2:
    #    continue
    if (x, y) == end_pos:
        print('DONE!', steps)
        exit()
    if ((x, y), steps) in visited:
        continue
    visited.add(((x, y), steps))

    if (x, y) in get_state(steps) or content[y][x] == '#':
        continue

    for dx, dy in deltas:
        tx = x+dx
        ty = y+dy
        if 0 <= tx < len(content[0]) and 0 <= ty < len(content):
            deq.append(((tx, ty), steps+1))
        deq.append(((x, y), steps+1))