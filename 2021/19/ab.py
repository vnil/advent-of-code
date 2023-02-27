# Take time to read
# Consider different approaches
# +-1 errors?
# Got last item?
# What is the diff between states? Pattern?


from collections import Counter
from collections import defaultdict, deque
from pprint import pprint as pp
from itertools import combinations, permutations
from copy import deepcopy
import math
import re
from queue import PriorityQueue
import json


def overlaps(arr1, arr2):
    s = defaultdict(int)
    tot = 0
    for c1 in arr1:
        for c2 in arr2:
            x = c1[0]-c2[0]
            y = c1[1]-c2[1]
            z = c1[2]-c2[2]
            tot += 1

            s[(x, y, z)] += 1
    for key in s:
        if s[key] >= 12:
            return (True, key)
    return (False, ())

def get_all_variants(arr):
    all_variants = []
    current = arr
    all_variants.append(current)
    for f in [rotate_z, rotate_z, rotate_z, rotate_z, rotate_x, rotate_x, rotate_x]:

        for _ in range(4):
            current = rotate_x(current)
            all_variants.append(current)

        for _ in range(4):
            current = rotate_y(current)
            all_variants.append(current)
        
        for _ in range(4):
            current = rotate_z(current)
            all_variants.append(current)
        

        current = f(current)

    return all_variants

def rotate_x(c):
    return (c[0], -c[2], c[1])

def rotate_y(arr):
    return (arr[2], arr[1], -arr[0])

def rotate_z(arr):
    return (-arr[1], arr[0], arr[2])

def create_obj(scanner_nr, current_data):
    obj = {'scanner': scanner_nr, 'raw': current_data, 'variants': [[] for _ in range(100)]}
    for k in current_data:
        variants = get_all_variants(k)
        for i,v in enumerate(variants):
            obj['variants'][i].append(v)
    return obj

content = open('i', 'r').readlines()
content = [c.strip() for c in content]

dists = set()

scanners = []
scanner_nr = 0
current_data = []
for row in content:
    if len(row) == 0:
        continue
    elif '---' in row:
        if not current_data:
            continue
        scanners.append(create_obj(scanner_nr, current_data))
        current_data = []
        scanner_nr += 1
    else:
        current_data.append([int(x) for x in row.split(',')])
if current_data:
    scanners.append(create_obj(scanner_nr, current_data))

poses = defaultdict(int)
all_beacons = set()

start_scanner_id = 0
scanner_variant_id = 0
d_stuff = (0, 0, 0)
queue = deque([(start_scanner_id, scanner_variant_id, d_stuff)])
visited = set()

while queue:
    scanner_id, variant_id, d = queue.popleft()
    if scanner_id in visited:
        continue
    visited.add(scanner_id)

    base_scanner = scanners[scanner_id]
    for va1 in base_scanner['variants'][variant_id]:
        xx, yy, zz = d
        all_beacons.add((va1[0]+xx,va1[1]+yy,va1[2]+zz))

    pv = base_scanner['variants'][variant_id]

    for target_scanner_id in range(len(scanners)):
        if target_scanner_id == scanner_id or target_scanner_id in visited:
            continue
        target_scanner = scanners[target_scanner_id]

        for target_scanner_variant_id in range(100):
            
            sv = target_scanner['variants'][target_scanner_variant_id]
            if not sv:
                continue

            ok, dstuff = overlaps(pv, sv)
            if ok:
                xx, yy, zz = d
                dx, dy, dz = dstuff
                xx+=dx
                yy+=dy
                zz+=dz
                queue.append((target_scanner_id, target_scanner_variant_id, (xx, yy, zz)))
                dists.add((xx, yy, zz))

                break


print('part1', len(all_beacons))
bb = list(all_beacons)
bb.sort()
#pp(bb)

ma = 0
for d in dists:
    for k in dists:
        ma = max(ma, abs(d[0]-k[0]) + abs(d[1]-k[1]) + abs(d[2]-k[2]))
print('part2', ma)