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

content = open(filename, 'r').readlines()
content = [c.strip() for c in content]
count = 0

for row in content:
    left, right = row.split(",")
    l1,l2 = left.split("-")
    r1,r2 = right.split("-")
    l1, l2, r1, r2 = int(l1), int(l2), int(r1), int(r2)
    
    if l1 >= r1 and l2 <= r2:
        count += 1
    elif r1 >= l1 and r2 <= l2:
        count += 1
print(count)

