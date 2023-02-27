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

c = 0
x = 1

su = 0

arr = ['.'] * 240

def cycle():
    global x, c, su
    c+=1
    if c == 20 or (c - 20) % 40 == 0:
        su += c * x
        print(c, x, x*c)


for row in content:
    if row == 'noop':
        cycle()
        continue
    else:
        op, val = row.split()
        cycle()
        cycle()
        x+=int(val)
cycle()

print(su)
