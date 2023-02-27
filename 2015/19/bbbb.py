# Take time to read
# Consider different approaches
# +-1 errors?
# Got last item?


from collections import Counter
from collections import defaultdict, deque
from pprint import pprint as pp
from itertools import combinations
from copy import deepcopy


def get_arr(s):
    current = ""
    arr = []
    for c in s:
        if c.isupper():
            arr.append(current)
            current = c
        else:
            current+=c
    if len(c) > 0:
        arr.append(current)
    return arr[1:]
    
fa = open('input', 'r').read()

a = fa.split('\n\n')
content = a[0].split('\n')
M = a[1]
MAX_LEN = 0
content = [c.strip() for c in content]

d = defaultdict(list)
for row in content:
    source, target = row.split(' => ')
    aq = get_arr(target)
    MAX_LEN = max(MAX_LEN, len(aq))
    d[source].append(aq)

available_replacements = d.keys()
goal = get_arr(M)

least = 99999
global_best_index = -1
visited = dict()

def go(current, check_index=0, steps=0):
    #print(current, check_index, steps)
    global k, global_best_index, least

    if len(current) > len(goal):
        return

    if check_index == len(goal):
        print("FOUND A WAY", steps)
        least = min(least, steps)
    if check_index >= len(current):
        return
    #print(check_index, current, goal)
    if current[check_index] == goal[check_index]:
        go(current, check_index+1, steps)

    if len(current) > check_index + MAX_LEN + 1:
        return

    a = tuple(current)
    if a in visited and visited[a] <= steps:
        return
    visited[a] = steps

    if current[check_index] not in d:
        return
    replacements = d[current[check_index]]
    for replacement in replacements:
        new = current[:check_index] + replacement
        if check_index < len(current) - 1:
            new+=current[check_index+1:]
        go(new, check_index, steps+1)

go(['e'])
print(least)
