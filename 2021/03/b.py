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

arr2 = deepcopy(content)
arr3 = deepcopy(content)
arr = deepcopy(content)


for i in range(len(arr2[0])):
    nr = [0] * len(content[0])
    for row in arr2:
        for j in range(len(row)):
            nr[j] += int(row[j])

    s = ''
    for n in nr:
        if n * 2 >= len(arr2):
            s += '1'
        else:
            s += '0'

    common = s
    uncommon = ''.join(['0' if c == '1' else '1' for c in s])
    if len(arr2) > 1:
        arr2 = [a for a in arr2 if a[i] == common[i]]

    if len(arr2) == 1:
        break

for i in range(len(arr3[0])):
    nr = [0] * len(content[0])
    for row in arr3:
        for j in range(len(row)):
            nr[j] += int(row[j])

    s = ''
    for n in nr:
        if n * 2 >= len(arr3):
            s += '1'
        else:
            s += '0'

    common = s
    uncommon = ''.join(['0' if c == '1' else '1' for c in s])
    if len(arr3) > 1:
        arr3 = [a for a in arr3 if a[i] == uncommon[i]]

    if len(arr3) == 1:
        break

print(int(arr2[0], 2) * int(arr3[0], 2))
