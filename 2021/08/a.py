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
k = 0
for row in content:
    first, second = row.split(' | ')
    signal_patterns = first.split()
    digits = second.split()
    for d in digits:
        if 2 <= len(d) <= 4 or len(d) == 7:
            k+=1
                        
print(k)