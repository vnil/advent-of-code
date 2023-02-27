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

content = open('i', 'r').readlines()
content = [c.strip() for c in content]

nr = [0] * len(content[0])
print(nr)


for row in content:
    for i in range(len(row)):
        nr[i] += int(row[i])

s = ""
for n in nr:
    if n >= (len(content) // 2):
        s += '1'
    else:
        s += '0'

a = int(s, 2)
b = ['0' if c == '1' else '1' for c in s]
b = int(''.join(b), 2)
print('---')
print(a*b)
