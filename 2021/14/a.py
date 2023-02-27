

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

#poly = "NNCB" # EX
poly = "SHPPPVOFPBFCHHBKBNCV" # PROD

content = open('i', 'r').readlines()
content = [c.strip() for c in content]

D = {}

for row in content:
    first, second = row.split(' -> ')
    D[first] = second

for aq in range(10):
    new_str = ''
    for i in range(len(poly)-1):
        check = poly[i] + poly[i+1]
        rep = D[check]
        new_str+=poly[i] + rep
    new_str += poly[-1]
    poly = new_str


q = Counter(poly)
ma = max(q.values())
mi = min(q.values())

print(ma-mi)