

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


p1 = 1
p2 = 5

s1 = 0
s2 = 0
dice = 0
count = 0

go = 1000


while s1 < go and s2 < go:
    count+=3
    roll = 0
    for i in range(1, 4):
        dice+=1
        if dice > 100:
            dice-=100
        roll+=dice
    

    p1 = (p1 + roll - 1) % 10 + 1
    s1 += p1

    if s1 >= 1000 or s2 >= 1000:
        break

    count+=3
    roll = 0
    for i in range(1, 4):
        dice+=1
        if dice > 100:
            dice-=100
        roll+=dice
    
    p2 = (p2 + roll - 1) % 10 + 1
    s2 += p2

a = s1 if s1 < s2 else s2

print(count * a)
    
