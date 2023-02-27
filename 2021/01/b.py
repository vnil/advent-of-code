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

l = list(map(int, content))

prev = sum(l[0:3])
now = 0
count = 0
for i, c in enumerate(l):
    if i < 3:
        continue
    now = prev - l[i-3] + l[i]
    if now > prev:
        count += 1
    prev = now
print(count)
