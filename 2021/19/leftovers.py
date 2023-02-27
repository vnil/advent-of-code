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
    for c1 in arr1:
        #c1 = tuple([int(x) for x in c1.split(',')])
        
        for c2 in arr2:
            #c2 = tuple([int(x) for x in c2.split(',')])
            x = c1[0]-c2[0]
            y = c1[1]-c2[1]
            z = c1[2]-c2[2]
            tot += 1
            x*=1_000_000
            y*=1000
            s[x+y+z] += 1
    return max(s.values()) >= 12

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

content = open('e', 'r').readlines()
content = [c.strip() for c in content]

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

xx = 0
yy = 0
zz = 0
done = set([0])
poses = defaultdict(int)
very_done = False
all_beacons = set()

start_scanner_id = 0
scanner_variant_id = 0
#print(scanners[0]['variants'])

while start_scanner_id != None:
    print("Scanning from ", start_scanner_id, scanner_variant_id)
    smack = False
    start_scanner = scanners[start_scanner_id]
    for va1 in start_scanner['variants'][scanner_variant_id]:
        all_beacons.add((va1[0]+xx,va1[1]+yy,va1[2]+zz))
    if very_done:
        break
    for s in range(len(scanners)):
        if smack:
            break
        if s in done or s == start_scanner_id:
            continue
        scanner = scanners[s]

        v1 = scanner_variant_id
        for v2 in range(100):
            if smack:
                break
           
            pv = start_scanner['variants'][v1]
            sv = scanner['variants'][v2]
            if not sv:
                continue
            for dx in range(-2010, 2011):
                count = 0
                for variant1 in pv:
                    for variant2 in sv:
                        if variant1[0] == variant2[0]+dx:
                            count+=1
                if count >= 12:
                    count = 0
                    for dy in range(-2010, 2011):
                        for variant1 in pv:
                            for variant2 in sv:
                                if variant1[0] == variant2[0]+dx and variant1[1] == variant2[1]+dy:
                                    count+=1
                        if count >= 12:
                            count = 0
                            for dz in range(-2010, 2011):
                                for variant1 in pv:
                                    for vid, variant2 in enumerate(sv):
                                        if variant1[0] == variant2[0]+dx and variant1[1] == variant2[1]+dy and variant1[2] == variant2[2]+dz:
                                            count+=1
                                            if count >= 12:
                                                if s in done:
                                                    break
                                                xx+=dx
                                                yy+=dy
                                                zz+=dz
                                                start_scanner_id = s
                                                scanner_variant_id = vid
                                                print(xx, yy, zz, 'to scanner', s, len(all_beacons), vid)
                                                done.add(s)
                                                smack = True
                                                if len(done) == len(scanners):
                                                    very_done = True

                                                break


print(len(all_beacons))