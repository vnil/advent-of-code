from collections import Counter
from collections import defaultdict, deque
from pprint import pprint as pp
from itertools import combinations
from copy import deepcopy


content = open('input', 'r').readlines()
content = [c.strip() for c in content]

arr = []

for row in content:
    parts = row.split()
    print(parts)
    arr.append((int(parts[3]), int(parts[11][:-1])))
print(arr)

delay = 0
while True:
    ok = True
    for index, (size, start) in enumerate(arr):
        if (start+delay+index+1) % size != 0:
            ok = False
            break
    if ok:
        print(delay, ':::')
        break
    delay += 1
