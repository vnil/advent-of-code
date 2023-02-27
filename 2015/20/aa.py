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
                s+=i+other
            else:
                s+=i
        i+=1
    return s*10

            
def calculate(nr):
    s = 0
    if i in dp:
        print("hit!")
        return dp[i]
    else:
        cur = calc(i)
        dp[i] = cur
        return cur
    

k = 0
#print(calc(2476767)) too high
for house_nr in range(1, 2476767+1):
    s=calc(house_nr)
    if s >= 33100000:
        print(house_nr)
        exit()
    if k%100000 == 0:
        print(house_nr, s)
    k+=1