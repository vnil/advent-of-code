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

q = []

for row in content:
    left, right = row.split(" ")
    q.append(d[left][right])

print(sum(q))
    

#A for Rock, B for Paper, and C for Scissors.

#X for Rock, Y for Paper, and Z for Scissors. 