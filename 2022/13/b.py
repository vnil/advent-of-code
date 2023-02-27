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

content = open(filename, 'r').read()
content = content.split('\n\n')
content = [c.strip() for c in content]


def compare(left, right):
    if isinstance(left, list) and isinstance(right, list):
        index = 0
        diff = 0
        while True:
            if len(left) == index and len(right) == index:
                return True, False
            if len(left) == index:
                return True, True
            if len(right) == index:
                return False, True


            res, decided = compare(left[index], right[index])
            if decided:
                return res, True
            index+=1
    if isinstance(left, list) and not isinstance(right, list):
        return compare(left, [right])
    elif not isinstance(left, list) and isinstance(right, list):
        return compare([left], right)
    else:
        return left <= right, left != right
        
a = [[[2]], [[6]]]
for (i, group) in enumerate(content):
    left, right = group.split('\n')
    
    left = eval(left)
    right = eval(right)
    a.append(left)
    a.append(right)
    
def ka(item1, item2):
    e, w = compare(item1, item2) 
    k = 1 if e else -1
    return k

a.sort(key=functools.cmp_to_key(ka))
a=list(reversed(a))
a = [str(r) for r in a]

k = 1
for i in range(len(a)):
    e = a[i]
    if e == '[[2]]':
        k*=i+1
    if e == '[[6]]':
        k*=i+1
print(k)