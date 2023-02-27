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

i = 0

group = []
for row in content:
    i+=1
    group.append(row)
    if i%3 == 0:
        
        print(group)
        s = set(group[0])
        for p in group[1:]:
            s = s.intersection(p)
            
        letter = list(s)[0]
        letter_code = ord(letter)

        if letter.isupper():
            letter_code -= 65 - 27
        else:
            letter_code -=96
        print(letter, letter_code)
        q.append(letter_code)


        group = []

    

print(sum(q))
    
    