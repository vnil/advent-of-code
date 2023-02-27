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

l = map(int, content)
c = 0
prev = math.inf
for i in l:
    if i > prev:
        c += 1
    prev = i
print(c)
