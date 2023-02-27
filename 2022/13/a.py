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

filename = sys.argv[1]

content = open(filename, 'r').read()
content = content.split('\n\n')
content = [c.strip() for c in content]

total = 0


def compare(left, right):
    #print(left, ' :: ', right)
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
            #if isinstance(right[index], int) and isinstance(left[index], int):
            #    diff = left[index] - right[index]
            #else:
            #    diff = 0
            if decided:
                return res, True
            index+=1
    if isinstance(left, list) and not isinstance(right, list):
        return compare(left, [right])
    elif not isinstance(left, list) and isinstance(right, list):
        return compare([left], right)
    else: # Both ints
        return left <= right, left != right
        
#592, 5400, 324

for (i, group) in enumerate(content):
    left, right = group.split('\n')
    
    left = eval(left)
    right = eval(right)

    ok, _ = compare(left, right)
    print("-----", ok)
    if ok:
        total += (i+1)
print("tot", total)
    

