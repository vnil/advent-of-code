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
score = 0

filename = sys.argv[1]

content = open(filename, 'r').readlines()
content = [c.strip() for c in content]

for i in range(0, len(content), 3):
    a,b,c = content[i], content[i+1], content[i+2]
    a = set(a) & set(b) & set(c)

    letter = list(a)[0]
    score += (ord(letter) - ord('a') + 1) if letter.islower() else (ord(letter) - ord('A') + 1 + 26)
print(score)