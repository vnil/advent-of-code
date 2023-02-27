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
import functools

filename = sys.argv[1]

content = open(filename, 'r').readlines()
content = [c.strip() for c in content]

M = int(sys.argv[2]) 

types = [
    'ore',
    'clay',
    'obsidian',
    'geode'
]
quality_levels = []

def add_arr(arr1, arr2):
    assert len(arr1) == len(arr2)
    arr = []
    for i in range(len(arr1)):
        arr.append(arr1[i] + arr2[i])
    return arr

#'ore','clay','obsidian','geode
for row in content[0:3]:
    parts = row.split()
    ids = int(parts[1][:-1])
    ore_robot_price_in_ore = int(parts[6])
    clay_robot_price_in_ore = int(parts[12])
    obsidian_robot_price_in_ore = int(parts[18])
    obsidian_robot_price_in_clay = int(parts[21])
    geode_robot_price_in_ore = int(parts[27])
    geode_robot_price_in_obsidian = int(parts[30])


    _robots = [1, 0, 0, 0]

    _wallet = [0, 0, 0, 0]
    maxi = 0

    mem = dict()
    best_at_minute = defaultdict(int)
    baba = defaultdict(int)
    obsidian_best_at_minute = defaultdict(int)
    #Har man samma antal robots, borde det ge samma diff till walleten. Borde gå att cachea
    
    def explore(minutes_left, robots, wallet):

        global mem, maxi

        ke = (minutes_left, robots, wallet)
        if ke in mem:
            return mem[ke]
        if minutes_left == 0:
            return wallet[3]





        d = min(wallet[0] // geode_robot_price_in_ore, wallet[2] // geode_robot_price_in_obsidian, 1)

        if best_at_minute[minutes_left] > robots[3] and baba[minutes_left] > wallet[3]:
           return -1
        elif best_at_minute[minutes_left] < robots[3] and baba[minutes_left] < wallet[3]:
           best_at_minute[minutes_left] = max(best_at_minute[minutes_left], robots[3])
           baba[minutes_left] = max(baba[minutes_left], wallet[3])
        # if wallet[2] > 0 and minutes_left > ko:
        #     ko = minutes_left
        #if best_at_minute[minutes_left] == robots[3]:
            #if obsidian_best_at_minute[minutes_left] > robots[2]:
            #    return -1
            #else:
            #    obsidian_best_at_minute[minutes_left] = robots[2]
        
        

        explored = []
        max_obsidian = min((wallet[0] - d * geode_robot_price_in_ore) // obsidian_robot_price_in_ore, wallet[1] // obsidian_robot_price_in_clay, 0 if d > 0 else 1)
        for c in reversed(range(max_obsidian + 1)):
            max_clay = min((wallet[0] - d*geode_robot_price_in_ore - c*obsidian_robot_price_in_ore) // clay_robot_price_in_ore, 0 if d+c > 0 else 1)
            for b in reversed(range(max_clay + 1)):
                max_ore = min((wallet[0] - d*geode_robot_price_in_ore - c*obsidian_robot_price_in_ore - b*clay_robot_price_in_ore) // ore_robot_price_in_ore, 0 if d+c+b > 0 else 1)
                for a in reversed(range(max_ore + 1)):
                    suggestion = [a, b, c, d]

                    new_wallet = (
                        wallet[0] + robots[0] - (a*ore_robot_price_in_ore +
                        b*clay_robot_price_in_ore +
                        c*obsidian_robot_price_in_ore +
                        d*geode_robot_price_in_ore),
                        wallet[1] + robots[1] - c*obsidian_robot_price_in_clay,
                        wallet[2] + robots[2] - d*geode_robot_price_in_obsidian,
                        wallet[3] + robots[3] 
                    )

                    new_robots = tuple(add_arr(robots, suggestion))

                    explored.append(explore(minutes_left - 1, new_robots, new_wallet))
        an = max(explored) if len(explored) > 0 else 0
        if maxi < an:
            print("maxi", an)
            maxi = an

        mem[ke] = an
        
        return an


    res = explore(M, tuple(_robots), tuple(_wallet))
    quality_levels.append(res)
    print('-- GEODE', res)


print(':ANS:', quality_levels[0]*quality_levels[1]*quality_levels[2], quality_levels)