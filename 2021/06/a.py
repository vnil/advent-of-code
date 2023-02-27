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

content = open('i', 'r').readlines()
l = list(map(int, content[0].split(',')))
l2=list(l)
old_length = 0
for day in range(1, 80+1):
    new_fishes = []
    for i in range(len(l)):
        if l[i] == 0:
            new_fishes.append(8)
            l[i] = 6
        else:
            l[i]-=1
    l += new_fishes
print(len(l))
