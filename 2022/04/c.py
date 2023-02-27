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

filename = '/Users/viktor/Documents/AoC/2022/04/ea'
#filename = 'i'

content = open(filename, 'r').readlines()
content = [c.strip() for c in content]