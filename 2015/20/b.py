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


dp = dict()

def calc(nr):
    sq = math.sqrt(nr)
    s = 0
    i = 1
    while i <= sq:
        if nr % i == 0:
            other = nr // i
            if other != i:
                if other*50 >= nr:
                    s+=other
                if i*50 >= nr:
                    s+=i
            else:
                if i*50 >= nr:
                    s+=i
        i+=1
    return s*11

k = 0
#4989600 high

highest = 0
for house_nr in range(0, 4989600):
    s=calc(house_nr)
    if s > highest:
        highest = s
        print('NEW high', s)
    if s >= 33100000:
        print('YES!', house_nr)
        exit()
    if k%100000 == 0:
        print(house_nr, s)
    k+=1