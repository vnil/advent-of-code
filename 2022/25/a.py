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
tot_sum = 0
for row in content:
    nr = ''.join(reversed(row))
    sm = 0
    for i in range(len(row)):
        real_part = 0
        if nr[i] == '-':
            real_part = -1
        elif nr[i] == '=':
            real_part = -2
        else:
            real_part = int(nr[i])
        sm+=(5**i)*real_part
    print(sm)
    tot_sum+=sm

print(tot_sum)


snafu = []




for i in range(30):
    left_over = (tot_sum//(5**i))%5
    print(tot_sum, left_over)
    cur = ""
    if left_over == 3:
        cur = '='
        tot_sum+=2*(5**i)
    elif left_over == 4:
        cur = '-'
        tot_sum+=1*(5**i)    
    else:
        cur = str(left_over)
    snafu.append(cur)


print(''.join(reversed(snafu)))
