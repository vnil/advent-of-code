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
cl = len(l)

d = defaultdict(int)

for val in l:
    d[val]+=1

for day in range(1, 256+1):
    c = deepcopy(d)
    for key,cnt in d.items():
        if key == 0:
            c[8]+=cnt
            c[6]+=cnt
            c[0]-=cnt
        else:
            c[key-1]+=cnt
            c[key]-=cnt
    d=c
print(sum(d.values()))
