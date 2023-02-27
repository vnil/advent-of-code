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
for row in content:
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
    obsidian_best_at_minute = defaultdict(int)
    hits = 0
    #Har man samma antal robots, borde det ge samma diff till walleten. Borde gå att cachea
    nonhits = 0
    ko = 0
    def explore(minutes_left, robots, wallet):
        qq=0

        global mem, maxi, hits, nonhits, ko


        #if M - minutes_left + 1 == 20 and wallet == (3, 21, 5, 1) and robots == (1, 4, 2, 1):
        #if M - minutes_left + 1 == 24 and wallet == (6, 41, 8, 9) and robots == (1, 4, 2, 2):
        #if M - minutes_left + 1 == 5 and wallet == (2, 1, 0, 0) and robots == (1, 1, 0, 0):
        #if M - minutes_left + 1 == 19 and wallet == (2, 17, 3, 0) and robots == (1, 4, 2, 1):
            #print("WOOOP", robots)
            #exit()

        ke = (minutes_left, robots, wallet)
        if ke in mem:
            hits +=1
            return mem[ke]
        nonhits += 1
        if minutes_left == 0:
            return wallet[3]




        #o_ore = wallet[0] // ore_robot_price_in_ore
        #o_clay = wallet[0] // clay_robot_price_in_ore
        #o_obsidian = min(wallet[0] // obsidian_robot_price_in_ore, wallet[1] // obsidian_robot_price_in_clay)
        #o_geode = min(wallet[0] // geode_robot_price_in_ore, wallet[2] // geode_robot_price_in_obsidian)

        d = min(wallet[0] // geode_robot_price_in_ore, wallet[2] // geode_robot_price_in_obsidian, 1)

        if best_at_minute[minutes_left] > robots[3]:
            return -1
        else:
            best_at_minute[minutes_left] = robots[3]
        # if wallet[2] > 0 and minutes_left > ko:
        #     ko = minutes_left
        #if best_at_minute[minutes_left] == robots[3]:
            #if obsidian_best_at_minute[minutes_left] > robots[2]:
            #    return -1
            #else:
            #    obsidian_best_at_minute[minutes_left] = robots[2]
        
        

        explored = []
        combs = 0
        max_obsidian = min((wallet[0] - d * geode_robot_price_in_ore) // obsidian_robot_price_in_ore, wallet[1] // obsidian_robot_price_in_clay, 1)
        for c in reversed(range(max_obsidian + 1)):
            max_clay = min((wallet[0] - d*geode_robot_price_in_ore - c*obsidian_robot_price_in_ore) // clay_robot_price_in_ore, 1)
            for b in reversed(range(max_clay + 1)):
                max_ore = min((wallet[0] - d*geode_robot_price_in_ore - c*obsidian_robot_price_in_ore - b*clay_robot_price_in_ore) // ore_robot_price_in_ore, 1)
                for a in reversed(range(max_ore + 1)):
                    suggestion = [a, b, c, d]
                    if a + b + c + d > 1:
                        continue
                    combs+=1

                    qq+=1
                    new_wallet = (
                        wallet[0] + robots[0] - (a*ore_robot_price_in_ore +
                        b*clay_robot_price_in_ore +
                        c*obsidian_robot_price_in_ore +
                        d*geode_robot_price_in_ore),
                        wallet[1] + robots[1] - c*obsidian_robot_price_in_clay,
                        wallet[2] + robots[2] - d*geode_robot_price_in_obsidian,
                        wallet[3] + robots[3] 
                    )

                    #if qq % 1000 == 0:

                    new_robots = tuple(add_arr(robots, suggestion))
                    #print(M-minutes_left+1, new_wallet, new_robots, suggestion)    


                    explored.append(explore(minutes_left - 1, new_robots, new_wallet))
        #print(combs, wallet)
        #print(qq)
        an = max(explored) if len(explored) > 0 else 0
        if maxi < an:
            print("maxi", an)
            maxi = an

        mem[ke] = an
        
        return an


    res = explore(M, tuple(_robots), tuple(_wallet))
    quality_levels.append(res * ids)
    print('-- GEODE', res)

    print('HITS', hits)
    print('NONHITS', nonhits)

print(':ANS:', sum(quality_levels), quality_levels)