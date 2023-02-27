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

content = open(filename, 'r').read()
q = [sum(list(map(int, a.split("\n")))) for a in content.split("\n\n")]
q.sort()
print(sum(q[-3:]))