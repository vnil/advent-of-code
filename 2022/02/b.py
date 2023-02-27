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


#A
d = {
    "A": {
        "X": 3 + 1,
        "Y": 6 + 2,
        "Z": 0 + 3
    },
    "B": {
        "X": 0 + 1,
        "Y": 3 + 2,
        "Z": 6 + 3
    },
    "C": {
        "X": 6 + 1,
        "Y": 0 + 2,
        "Z": 3 + 3
    },
}

m = {
    "A": {
        "X": "Z", # loose
        "Y": "X", # draw
        "Z": "Y"  # win
    },
    "B": {
        "X": "X",
        "Y": "Y",
        "Z": "Z"
    },
    "C": {
        "X": "Y",
        "Y": "Z",
        "Z": "X"
    },
}

q = []

for row in content:
    left, right = row.split(" ")
    mapped = m[left][right]
    q.append(d[left][mapped])

print(sum(q))
    
