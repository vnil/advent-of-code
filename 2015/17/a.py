# Take time to read
# Consider different approaches
# +-1 errors?
# Got last item?


from collections import Counter
from collections import defaultdict, deque
from pprint import pprint as pp
from itertools import combinations


content = open('input', 'r').readlines()
content = sorted([int(c.strip()) for i, c in enumerate(content)])


p1 = 0
m = 99999
for i in range(len(content)):
    for comb in combinations(content, i):
        if sum(comb) == 150:
            m = min(m, len(comb))
            p1 += 1
print(p1)
p2 = 0
for comb in combinations(content, m):
    if sum(comb) == 150:
        p2 += 1
print(p2)
