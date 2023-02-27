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
    pos = c % 40
    if x == pos or x == pos - 1 or x == pos + 1:
        arr[c] = '#'
    c+=1
    print(c)
    


for row in content:
    if row == 'noop':
        cycle()
        continue
    else:
        op, val = row.split()
        cycle()
        cycle()
        x+=int(val)

print(''.join(arr[0:40]))
print(''.join(arr[40:80]))
print(''.join(arr[80:120]))
print(''.join(arr[120:160]))
print(''.join(arr[160:200]))
print(''.join(arr[200:]))

