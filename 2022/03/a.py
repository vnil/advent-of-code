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

q = []

for row in content:
    l = len(row) // 2
    left = row[0:l]
    right = row[l:]
    left_set = set(left)
    right_set = set(right)

    letter = list(left_set.intersection(right_set))[0]
    letter_code = ord(letter)

    if letter.isupper():
        letter_code -= 65 - 27
    else:
        letter_code -=96
    print(letter, letter_code)
    #print(letter_code)
    q.append(letter_code)
    

print(sum(q))
    
    