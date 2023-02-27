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

def add_arr(arr1, arr2):
    assert len(arr1) == len(arr2)
    arr = []
    for i in range(len(arr1)):
        arr.append(arr1[i] + arr2[i])
    return arr

#'ore','clay','obsidian','geode
for row in content:
    parts = row.split()
    ids = int(parts[1][:1])
    ore_robot_price_in_ore = int(parts[6])
    clay_robot_price_in_ore = int(parts[12])
    obsidian_robot_price_in_ore = int(parts[18])
    obsidian_robot_price_in_clay = int(parts[21])
    geode_robot_price_in_ore = int(parts[27])
    geode_robot_price_in_obsidian = int(parts[30])

    _robots = [1, 0, 0, 0]

    _wallet = [0, 0, 0, 0]


    di = dict()

    kood = defaultdict(int)
 
    def explore(minutes_left, robots, wallet):
        global di
        ke = (minutes_left, robots, wallet)
        if ke in di:
            return di[ke]

        if minutes_left == 0:
            return wallet[3]

        if kood[minutes_left] > wallet[3]:
            return -1

        #find explore different ways to consume
        
        
        
        explored = []

        new_wallet = list(wallet)
        for i in range(4):    
            #end of the minute
            new_wallet[i] += robots[i]
        new_wallet = tuple(new_wallet)
        


        o_ore = wallet[0] // ore_robot_price_in_ore
        o_clay = wallet[0] // clay_robot_price_in_ore
        o_obsidian = min(wallet[0] // obsidian_robot_price_in_ore, wallet[1] // obsidian_robot_price_in_clay)
        o_geode = min(wallet[0] // geode_robot_price_in_ore, wallet[2] // geode_robot_price_in_obsidian)

        d = o_geode
        if d > 0:
            print("woo")
        ore_spent = d * geode_robot_price_in_ore


        for a in reversed(range(o_ore + 1)):
            ore_spent =  a * ore_robot_price_in_ore + d * geode_robot_price_in_ore
            if ore_spent > wallet[0]:
                    continue
            for b in reversed(range(o_clay + 1)):
                ore_spent =  a * ore_robot_price_in_ore + b * clay_robot_price_in_ore + d * geode_robot_price_in_ore
                if ore_spent > wallet[0]:
                    continue
                for c in reversed(range(o_obsidian + 1)):
                    ore_spent = a * ore_robot_price_in_ore + b * clay_robot_price_in_ore + c * obsidian_robot_price_in_ore + d * geode_robot_price_in_ore
                    if ore_spent > wallet[0]:
                        continue

                    suggestion = [a, b, c, d]
                    spent = []
                    spent.append(
                        suggestion[0]*ore_robot_price_in_ore +
                        suggestion[1]*clay_robot_price_in_ore +
                        suggestion[2]*obsidian_robot_price_in_ore +
                        suggestion[3]*geode_robot_price_in_ore
                    )
                    spent.append(suggestion[2]*obsidian_robot_price_in_clay)
                    spent.append(suggestion[3]*geode_robot_price_in_obsidian)
                    spent.append(0)
                    #print(spent[0], ore_spent)
                    assert spent[0] == ore_spent

                    ok = True

                    for i in range(4):
                        if spent[i] > wallet[i]:
                            ok = False
                            break

                    if not ok:
                        continue
                    

                    new_robots = tuple(add_arr(robots, suggestion))

                    explored.append(explore(minutes_left - 1, new_robots, new_wallet))


        an = max(explored)
        di[ke] = an
        kood[minutes_left] = an
        return an


    print(explore(M, tuple(_robots), tuple(_wallet)))

    