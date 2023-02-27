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

content = open('i', 'r').readlines()
content = [c.strip() for c in content]
x = 0
y = 0
aim = 0
for row in content:
    right, left = row.split()
    left = int(left)
    if right == "forward":
        x += left
    if right == "up":
        y -= left
        aim -= left
    if right == "down":
        y += left
        aim += left
print(x*y)
