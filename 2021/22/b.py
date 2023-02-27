

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

content = open('i', 'r').readlines()
content = [c.strip() for c in content]

#on x=-11829..-1061,y=19988..32790,z=-92294..-55506
#off x=21352..40945,y=40771..48583,z=-67151..-59151

instructions = []

for row in content:
    second = ''
    first = row.split(' ')[0]
    if first == 'on':
        second = row[3:]
    else:
        second = row[4:]
    parts = second.split(',')
    arr = []
    for part in parts:
        cord, ran = part.split('=')
        small, large = [int(a) for a in ran.split('..')]
        if small > large:
            large, small = small, large
        arr.append((small, large))
    instructions.append((first, arr))


grid = defaultdict(int)
on = 0
off = []

def find_intersection(cube1, cube2):
    x_min = max(cube1[0][0], cube2[0][0])
    x_max = min(cube1[0][1], cube2[0][1])
    y_min = max(cube1[1][0], cube2[1][0])
    y_max = min(cube1[1][1], cube2[1][1])
    z_min = max(cube1[2][0], cube2[2][0])
    z_max = min(cube1[2][1], cube2[2][1])

    if x_min > x_max or y_min > y_max or z_min > z_max:
        return None
    
    return ((x_min, x_max), (y_min, y_max), (z_min, z_max))

def merge(cube1, cube2):
    new_cubes = []
    if cube1[2][0] > cube2[2][0]:
        cube2, cube1 = cube1, cube2
    z_min = cube1[2][0]
    z_max = cube2[2][0]-1
    #First: Simple single part
    if z_min <= z_max:
        new_cubes.append([cube1[0], cube1[1], (z_min, z_max)])
    #Second: Complex multiple cubes

    #left
    z_min = z_max+1
    z_max = min(cube1[2][1], cube2[2][1])

    x_max = max(cube1[0][0], cube2[0][0])-1
    if cube1[0][0] != cube2[0][0]:
        leftmost_cube = cube1 if cube1[0][0] < cube2[0][0] else cube2
        new_cubes.append([(leftmost_cube[0][0], x_max), leftmost_cube[1], (z_min, z_max)])

    #middle
    x_min = x_max+1
    x_max = min(cube1[0][1], cube2[0][1])

    ### Sub
    low_cube = cube1 if cube1[1][0] < cube2[1][0] else cube2
    high_cube = cube2 if cube1 == low_cube else cube1

    y_low = low_cube[1][0]
    y_above = high_cube[1][0]-1
    new_cubes.append([(x_min, x_max), (y_low, y_above), (z_min, z_max)])

    y_low = y_above+1
    y_above = min(low_cube[1][1], high_cube[1][1])
    new_cubes.append([(x_min, x_max), (y_low, y_above), (z_min, z_max)])

    y_low = y_above+1
    y_above = max(low_cube[1][1], high_cube[1][1])

    new_cubes.append([(x_min, x_max), (y_low, y_above), (z_min, z_max)])
    ### Sub



    #y_min = min(cube1[1][0], cube2[1][0])
    #y_max = max(cube1[1][1], cube2[1][1])

    #new_cubes.append([(x_min, x_max), (y_min, y_max), (z_min, z_max)])

    #right
    x_min = x_max+1
    x_max = max(cube1[0][1], cube2[0][1])
    if x_min <= x_max:
        rightmost_cube = cube1 if cube1[0][1] > cube2[0][1] else cube2
        new_cubes.append([(x_min, x_max), (rightmost_cube[1][0], rightmost_cube[1][1]), (z_min, z_max)])

    #Third: Simple single part
    z_min = z_max+1
    z_max = max(cube1[2][1], cube2[2][1])
    if z_min <= z_max:
        deepest = cube1 if cube1[2][1] > cube2[2][1] else cube2
        new_cubes.append([deepest[0], deepest[1], (z_min, z_max)])
    
    return new_cubes
        
    
def volume(cube):
    return (cube[0][1] - cube[0][0]+1) * (cube[1][1] - cube[1][0]+1) * (cube[2][1] - cube[2][0]+1) 


on = []

for inst in instructions:
    should_on, org_cube = inst
    added = False
    
    #Find intersection => Split in parts, remove subcubes intersecting with existing cube
    if should_on == 'on':
        leftovers = [org_cube]
        for existing_cube in on:
            new_leftovers = []
            for cube in leftovers:
                intersection = find_intersection(existing_cube, cube)
                if intersection:
                    if existing_cube == cube:
                        continue
                    #If on and intersection, instead add the merged parts of these two
                    pieces = merge(existing_cube, cube)
                    for piece in pieces:
                        if not find_intersection(piece, existing_cube):
                            new_leftovers.append(piece)
                else:
                    new_leftovers.append(cube)
            leftovers = new_leftovers
        for q in leftovers:
            on.append(q)
    else:
        new_on = []
        removal_cube = org_cube
        while on:
            existing_cube = on.pop()
            intersection = find_intersection(existing_cube, removal_cube)
            if intersection:
                if existing_cube == removal_cube:
                    continue
                pieces = merge(existing_cube, removal_cube)
                for piece in pieces:
                    if not find_intersection(piece, removal_cube):
                        new_on.append(piece)
            else:
                new_on.append(existing_cube)
        on = new_on



    vol = 0

    for cube in on:
        vol+=volume(cube)
print(vol)
