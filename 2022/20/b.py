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


class LinkNode:
    def __init__(self, val, _next = None, prev = None):
        self.val = val
        self.next = _next
        self.prev = prev

def print_list(l, max_count):
    s = ""
    n = l
    i = 0
    while n and i < max_count:
        i+=1
        s += str(n.val) + " -> "
        n = n.next
    print(s)

def print_list_back(l, max_count):
    s = ""
    n = l
    i = 0
    while n and i < max_count:
        i+=1
        s += str(n.val) + " -> "
        n = n.prev
    print(s)

def swap(item):
    sec = item.next
    secsec = sec.next
    prev = item.prev


    prev.next = sec
    item.next = secsec
    sec.next = item
    

    secsec.prev = item
    item.prev = sec
    sec.prev = prev

def move(item, steps):
    val = steps
    if val == 0:
        return


    
    if val > 0:
        #move forward
        while val > 0:
            swap(item)
            val-=1

    if val < 0:
        while val < 0:
            swap(item.prev)
            val+=1



filename = sys.argv[1]

content = open(filename, 'r').readlines()
content = [c.strip() for c in content]

last = None
zero_node = None

items = []
for i,row in enumerate(reversed(content)):
    n = int(row)*811589153
    link = LinkNode(n)
    items.append(link)

    if n == 0:
        zero_node = link
items.reverse()


for i in range(len(items)):
    items[i].next = items[(i+1)%len(items)]
    items[i].prev = items[i-1]




ans = []
print_list(items[0], 7)
for x in range(10):
    for item in items:


        le = item.val % (len(items)-1)
        #if item.val < 0:
        #    le-=1
        #print(le)
        move(item, le)
    print_list(items[0], 7)
        


c = zero_node
vals = []
for i in range(3001):
    
    
    if i%1000 == 0:
        vals.append(c.val)
    c = c.next
    


print(vals, sum(vals))