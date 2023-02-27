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
    item.next = sec.next
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

arr=[]
last = None
zero_node = None


for i,row in enumerate(reversed(content)):
    n = int(row)
    arr.append(n)
    link = LinkNode(n, last)
    if n == 0:
        zero_node = link
    last = link


first = last
last = first
while last.next:
    last = last.next
v = first

items = []

while v:
    items.append(v)
    v = v.next

prev = last
current = first
for item in items:
    item.prev = prev
    prev = item


last.next = first


#print_list(first, 7)



ans = []
print_list(items[0], 7)

for item in items:
    move(item, item.val)
    #print_list(zero_node, 7)
    
print("ok")
c = zero_node
vals = []
for i in range(3001):
    
    
    if i%1000 == 0:
        vals.append(c.val)
    c = c.next
    


print(vals, sum(vals))