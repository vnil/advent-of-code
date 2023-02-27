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

s = content[0]

d = defaultdict(int)

for (i, c) in enumerate(s):
    if len([a for a in d.values() if a > 0]) == 14:
        print(i)
        break
    d[c] += 1
    if i >= 14:
        d[s[i-14]] -= 1


window_size = 4 # 14

for i in range(window_size, len(s)):
    if len(set(s[i-window_size:i])) == window_size:
        print(i)
        break