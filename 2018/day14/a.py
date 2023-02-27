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

the_input = 18
#the_input = 793031
p1 = 0
p2 = 1

arr = [3, 7]

while len(arr) < the_input + 10:
    res = arr[p1] + arr[p2]
    if res > 9:
        a, b = list(map(int, str(res)))
        arr.append(a)
        arr.append(b)
    else:
        arr.append(res)
    p1 = (p1 + 1 + arr[p1]) % len(arr)
    p2 = (p2 + 1 + arr[p2]) % len(arr)

print(''.join(map(str, arr[-10:])))
