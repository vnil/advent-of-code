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




sums = []

s = 0
for a in content:
    if len(a) == 0:
        sums.append(s)
        s = 0
    else:
        s+=int(a)

sums.append(s)

print(sums)
print(max(sums))

