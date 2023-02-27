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
import functools

filename = sys.argv[1]

content = open(filename, 'r').readlines()
content = [c.strip() for c in content]
g = dict()
rates = dict()
interesting_pipes = ['AA']
M = int(sys.argv[2]) 

# Parsing
for row in content:
    parts = row.split()
    name = parts[1]
    rate = parts[4][5:-1]
    k = row.split('valve')
    rest = k[1][1:].strip().split(',')
    connections = [a.strip() for a in rest]
    g[name] = connections
    rates[name] = int(rate)
    if int(rate) > 0:
        interesting_pipes.append(name)

connections = defaultdict(dict)
max_pressure = sum(rates.values())

# Extract shortest paths
for i, a in enumerate(interesting_pipes):
    for b in interesting_pipes[i:]:
        if a == b:
            continue
        q = deque([(a, [a])])
        target = b
        visited = set()
        while q:
            current, path = q.popleft()
            if current in visited:
                continue
            visited.add(current)
            if current == target:
                connections[a][target] = list(reversed(path)) #Reveersed to allow popping instead
                connections[target][a] = path

                break
            for potential in g[current]:
                q.append((potential, list(path) + [potential]))


pipes = g.keys()
interesting_pipes = interesting_pipes[1:]


#print(connections['HH']['JJ'])

#exit()
def get_new_entries(arr, opened):
    new_round = []
    if len(arr) > 1:
        new_me = list(arr)
        new_me.pop()
        new_round.append((new_me, 0, opened))
    else:
        if arr[0] not in opened:
            new_set = set(opened)
            new_set.add(arr[0])
            new_round.append((arr, rates[arr[0]], new_set))
        for pipe in interesting_pipes:
            if pipe == arr[0]:
                continue

            new_round.append((connections[arr[0]][pipe][0:-1], 0, opened))

            
    return new_round

visited = set()
q = deque([])
visited = set()
for me_target in interesting_pipes:
    for elephant_target in interesting_pipes:
        if me_target == 'AA' or elephant_target == 'AA':
            continue
        if me_target == elephant_target:
            continue
        q.append((connections['AA'][me_target], connections['AA'][elephant_target], 0, set(), 0, 0))


max_p = 0
i=1
rr = defaultdict(lambda: -1)
while q:
    #pp(q)
    i+=1
    if i%100000 == 0:
        print(len(q), max_p)


    me, elephant, minute, opened, pressure, acc = q.popleft()
    ok = ''.join(sorted(opened))
    key = (me[-1], elephant[-1], ok, minute) # pressure might not work as key
    #print(key)
    #break
    if rr[key] > acc:
       continue
    rr[key] = acc
    rr[(elephant[-1], me[-1], ok, minute)] = acc
    if minute == M:
        #print(acc)
        if acc > max_p:
            print('TIME OVER', acc)
            max_p = acc
        continue

    if pressure == max_pressure:
        n = acc+pressure*(M-minute)
        best = minute
        if n > max_p:
            print('MAX PRESSURE', n)
            max_p = n
        
        continue
    a = get_new_entries(me, opened)
    b = get_new_entries(elephant, opened)

    if i == 1:
        break
    for alt_me in a:
        for alt_elephant in b:
            if alt_me[0][-1] == alt_elephant[0][-1] and (alt_me[1] > 0 and alt_elephant[1] > 0): ## Ca
                continue
            if alt_me[0][0] == alt_elephant[0][0]:
                continue

            new_opened = set(opened) | alt_me[2] | alt_elephant[2]
            new_pressure = pressure + alt_me[1] + alt_elephant[1]
            new_acc = acc+pressure
            
            ok = ''.join(sorted(new_opened))
            key = (alt_me[0][-1],  alt_elephant[0][-1], ok, minute+1) # pressure might not work as key
            if rr[key] > acc:
                continue

            q.append((alt_me[0], alt_elephant[0], minute+1, new_opened, new_pressure, new_acc))
    #pp(q)
    


print(max_p)
