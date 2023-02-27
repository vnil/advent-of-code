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
from functools import lru_cache

def roll_posibilities():
    rolls = defaultdict(int)
    for a in range(1, 4):
        for b in range(1, 4):
            for c in range(1, 4):
                rolls[a+b+c] +=1
    return rolls

rolls = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
d1 = defaultdict(int)

@lru_cache(maxsize=10000000)
def play1(score1, position1, score2, position2):
    if score2 >= 21:
        return 1
    s = 0
    for key in rolls:
        new_position1 = (position1 + key - 1) % 10 + 1
        if score1 + new_position1 >= 21:
            s += 1 * 100000000000000000000000000 * rolls[key]
            continue
        for k2 in rolls:
            new_position2 = (position2 + k2 - 1) % 10 + 1
            s += play1(score1 + new_position1, new_position1, score2 + new_position2, new_position2) * rolls[key]*rolls[k2]
    return s

print(play1(0, 1, 0, 5))
print('manually take out left and right number and determind the answer')

