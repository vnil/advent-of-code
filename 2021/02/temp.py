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

content = open('e', 'r').readlines()
content = [c.strip() for c in content]
x = 0
y = 0
aim = 0
for row in content:
    inst, val = row.split()
    val = int(val)
    if inst == "forward":
        x += val
        y += val*aim
    if inst == "up":
        aim -= val
    if inst == "down":
        aim += val
print(y*x)
