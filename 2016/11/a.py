from collections import Counter
from collections import defaultdict, deque
from pprint import pprint as pp
from itertools import combinations
from copy import deepcopy


content = open('input', 'r').readlines()
content = [c.strip() for c in content]

for row in content:
