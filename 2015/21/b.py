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
import re

def nums(s):
    return list(map(int, re.findall(r'\d+', s)))


weapons_str = """Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0"""

armors_str = """Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5"""

rings_str = """Damage +    25     1       0
Damage +    50     2       0
Damage +   100     3       0
Defense +   20     0       1
Defense +   40     0       2
Defense +   80     0       3"""

weapons = [nums(a) for a in weapons_str.split('\n')]
armors = [nums(a) for a in armors_str.split('\n')]
rings = [nums(a) for a in rings_str.split('\n')]

to_try = []

for w_cost, w_damage, w_armor in weapons:
    t_cost = w_cost
    t_damage = w_damage
    t_armor = w_armor

    to_try.append((w_cost, w_damage, w_armor))

    for a_cost, a_damage, a_armor in armors:
        to_try.append((w_cost + a_cost, w_damage + a_damage, w_armor + a_armor))

        for r1_cost, r1_damage, r1_armor in rings:
            to_try.append((
                w_cost + a_cost + r1_cost, 
                w_damage + a_damage + r1_damage, 
                w_armor + a_armor + r1_armor
            ))

            to_try.append((
                w_cost + r1_cost, 
                w_damage + r1_damage, 
                w_armor + r1_armor
            ))

            for r2_cost, r2_damage, r2_armor in rings:
                if r1_cost == r2_cost: # Price is unique amoung rings. Cant use two of same
                    continue
                to_try.append((
                    w_cost + a_cost + r1_cost + r2_cost, 
                    w_damage + a_damage + r1_damage + r2_damage, 
                    w_armor + a_armor + r1_armor + r2_armor
                ))

                to_try.append((
                    w_cost + r1_cost + r2_cost, 
                    w_damage + r1_damage + r2_damage, 
                    w_armor+ r1_armor + r2_armor
                ))

score = 0


"""
Hit Points: 104
Damage: 8
Armor: 1
"""

def is_win(damage, armor):
    p_life = 100
    b_life = 104
    b_damage = 8
    b_armor = 1

    while p_life > 0 and b_life > 0:
        b_life-=max(1, damage-b_armor)
        if b_life > 0:
            p_life-=max(1, b_damage-armor)
    return p_life > b_life

for cost, damage, armor in to_try:
    if not is_win(damage, armor):
        score = max(score, cost)
print(score)

#141 too low