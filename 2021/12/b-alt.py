from collections import defaultdict
import time

start_time = time.time()

content = open('i', 'r').readlines()
content = [c.strip() for c in content]

G = defaultdict(list)
count = 0

for row in content:
    left, right = row.split('-')
    G[left].append(right)
    G[right].append(left)

def dfs(node, V, using_twice):
    global count
    mod_twice = False
    if node == 'end':
        count+=1
        return
    if node in V and node.islower():
        if node == 'start':
            return
        elif using_twice:
            return
        
        using_twice = True
        mod_twice = True
        
    if node.islower():
        V.add(node)

    for child in G[node]:
        dfs(child, V, using_twice)

    if node.islower() and not mod_twice:
        V.remove(node)

dfs('start', set(), False)

print(count)
print("--- %s seconds ---" % (time.time() - start_time))