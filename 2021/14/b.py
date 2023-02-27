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

points = defaultdict(int)
A = defaultdict(int)

for i in range(len(poly) - 1):
    check = poly[i] + poly[i+1]
    points[check] += 1
    A[poly[i]]+=1
A[poly[-1]]+=1

for aq in range(40):
    cpoints = defaultdict(int)
    for check in points:
        score = 1
        if check in points:
            score = points[check]
        rep = D[check]
        cpoints[check[0] + rep] += score
        cpoints[rep + check[1]] += score
        A[rep] += score
    points = cpoints

ma = max(A.values())
mi = min(A.values())
print(ma-mi)


