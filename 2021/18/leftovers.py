

# Take time to read
# Consider different approaches
# +-1 errors?
# Got last item?
# What is the diff between states? Pattern?


from collections import Counter
from collections import defaultdict, deque
from pprint import pprint as pp
from itertools import combinations
from copy import deepcopy
import math
import re
from queue import PriorityQueue
import json

def addition(a, b):
    new_arr = []
    new_arr.append(a)
    new_arr.append(b)
    return new_arr


    

carry = None
prev = None
prev_side = 0

def explode_second(current, parent, replaces):
    global carry
    global prev
    global prev_side

    print(current, prev, prev_side)

    if isinstance(current, list):
        left, right = current
        prev_side = 0

        res = explode_second(left, current, replaces)
        if res:
            return True

    if not isinstance(current, list):
        if current == 'X':
            val1, val2 = replaces.popleft()
            if prev:
                print(prev[(prev_side + 1) % 2])
                prev[(prev_side + 1) % 2] += val1
                carry = val2
            if prev_side == 0 and not isinstance(parent[1], list):
                parent[1] += val2
                carry = None
                return True
        return
            
    
    prev = current
    prev_side = 1

    if carry:
        if not isinstance(current[0], list):
            current[0]+=carry
            carry = None
            return True
        elif not isinstance(current[1], list):
            current[1]+=carry
            carry = None
            return True

    return explode_second(right, current, replaces)

def explode_third(current):
    if current == 'X':
        return 0
    if not isinstance(current, list):
        return current
    return [explode_third(current[0]), explode_third(current[1])]


def explode(a):
    found = False
    carry = None
    prev = None
    prev_side = 0

    def explode_first(current, repl, depth = 0):
        nonlocal found
        if not isinstance(current, list):
            return current

        left, right = current
        
        first = explode_first(left, repl, depth+1)

        if depth >= 4 and not found:
            repl.append(current)
            found = True
            return 'X'

        second = explode_first(right, repl, depth+1)

        return [first, second]



    a = deepcopy(a)
    replaces = deque([])
    exps = explode_first(a, replaces)
    if not replaces:
        return (False, a)
    print('EXP', exps)
    carry = None
    prev = None
    prev_side = 0
    explode_second(exps, exps, replaces)
    third = explode_third(exps)
    return (True, third) 

def split(a):
    has_split = False

    def split_it(a):
        if not isinstance(a, list):
            if a > 9 and not has_split:
                left = a // 2
                right = a - left
                has_split = True
                return [left, right]
            return a
        return [split_it(a[0]), split_it(a[1])]
    split_it(a)
    print(has_split)
    return has_split






content = open('e', 'r').readlines()
#content = [[int(x) for x in c.strip()] for c in content]
content = [json.loads(c.strip()) for c in content]

current = content[0]

for i in range(1, len(content)):
    current = addition(current, content[i])
    while True:
        print('EXPL', current)
        success, new_current = explode(current)
        if success:
            current = new_current
            continue
        print('SPLIT')
        success = split(current)
        

        if success:
            continue
        break
    print(current)