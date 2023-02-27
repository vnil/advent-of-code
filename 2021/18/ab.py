

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

###### NODE ######

class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
    def __str__(self):
        return str(self.val) + 'n'

def isint(val):
    return not isinstance(val, list)

def nodeify(arr):
    start = Node('FAKE')
    prev_node = start

    def trav_node(data):
        if isint(data):
            return Node(data)
        return [trav_node(data[0]), trav_node(data[1])]

    def trav_link(node_or_arr):
        nonlocal prev_node
        if isinstance(node_or_arr, Node):
            prev_node.next = node_or_arr
            node_or_arr.prev = prev_node
            prev_node = node_or_arr
            return
        trav_link(node_or_arr[0])
        trav_link(node_or_arr[1])
    
    node_arr = trav_node(arr)
    trav_link(node_arr)
    real_start = start.next
    real_start.prev = None

    return (real_start, node_arr)

def denodify(data):
    if isinstance(data, Node):
        return data.val
    return [denodify(data[0]), denodify(data[1])]


#print(nodeify([[1, 2], 3]))

#exit()
###### NODE END ######

def alternative_second(current, replaces):
    if isinstance(current, Node):
        if current.val == 'X':
            val1, val2 = replaces.popleft()
            if current.prev:
                current.prev.val += val1
            if current.next:
                current.next.val += val2
            current.val = 0
            return True
        return
            
    left, right = current

    if alternative_second(left, replaces):
        return True
    return alternative_second(right, replaces)


def addition(a, b):
    new_arr = []
    new_arr.append(a)
    new_arr.append(b)
    return new_arr




def explode(a):
    found = False

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
    start_node, node_array = nodeify(exps)
    alternative_second(node_array, replaces)

    normal = denodify(node_array)
    return (True, normal) 


def split(a):
    has_split = False
    a = deepcopy(a)
    def split_it(a):
        nonlocal has_split
        if not isinstance(a, list):
            if a > 9 and not has_split:
                left = a // 2
                right = a - left
                has_split = True
                return [left, right]
            return a
        return [split_it(a[0]), split_it(a[1])]
    splitted_arr = split_it(a)
    
    return has_split, splitted_arr

def magnitude(arr):
    global maxa
    val1 = arr[0] if isint(arr[0]) else magnitude(arr[0])
    val2 = arr[1] if isint(arr[1]) else magnitude(arr[1])
    return val1 * 3 + val2 * 2


content = open('i', 'r').readlines()
content = [json.loads(c.strip()) for c in content]

current = content[0]

for i in range(1, len(content)):
    current = addition(current, content[i])
    while True:
        success, new_current = explode(current)
        if success:
            current = new_current
            continue
        success, new_current = split(current)
        if success:
            current = new_current
            continue
        break
    #print(current)
print('part1', magnitude((current)))

maxa = 0


for i in range(len(content)):
    for j in range(len(content)):
        if i == j:
            continue
        current = addition(content[i], content[j])
        while True:
            success, new_current = explode(current)
            if success:
                current = new_current
                continue
            success, new_current = split(current)
            if success:
                current = new_current
                continue
            break
        maxa = max(maxa, magnitude((current)))

print('part2', maxa)