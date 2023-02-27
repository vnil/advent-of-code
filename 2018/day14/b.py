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

the_input = "59414"
the_input = "793031"

s_input = str(the_input)
l_input = len(s_input)
p1 = 0
p2 = 1

arr = [3, 7]
sliding_arr = deque([3, 7])
c = 0


def add_and_check(val):
    arr.append(val)
    sliding_arr.append(val)
    if len(sliding_arr) > l_input:
        sliding_arr.popleft()
    if s_input == ''.join(map(str, sliding_arr)):
        print('Length', len(arr) - l_input)
        exit()


while True:
    res = arr[p1] + arr[p2]
    if res > 9:
        a, b = list(map(int, str(res)))
        add_and_check(a)
        add_and_check(b)
    else:
        add_and_check(res)

    p1 = (p1 + 1 + arr[p1]) % len(arr)
    p2 = (p2 + 1 + arr[p2]) % len(arr)
