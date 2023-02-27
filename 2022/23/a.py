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

g = defaultdict(lambda: '.')

for r, row in enumerate(content):
    for c, char in enumerate(row):
        if char == '#':
            g[(r, c)] = '#'


#pp(g.keys())

min_r = 999
max_r = 0
min_c = 999
max_c = 0

for i in range(10000000):
    keys = list(g.keys())
    suggestions = dict()
    for r, c in keys:
        if g[(r, c)] != '#':
            continue
        #first check if all is free
        ok = False
        for tr in range(-1, 2):
            for tc in range(-1, 2):
                if tr == 0 and tc == 0:
                    continue
                if g[(r+tr, c+tc)] == '#':
                    ok = True
                    break
        if not ok:
            continue
        sug = deque()
        if g[(r-1, c-1)] == '.' and g[(r-1, c)] == '.' and g[(r-1, c+1)] == '.':
            sug.append(((r-1, c), 'N'))
        else:
            sug.append((None, 'N'))
        if g[(r+1, c-1)] == '.' and g[(r+1, c)] == '.' and g[(r+1, c+1)] == '.':
            sug.append(((r+1, c), 'S'))
        else:
            sug.append((None, 'S'))
        if g[(r, c-1)] == '.' and g[(r-1, c-1)] == '.' and g[(r+1, c-1)] == '.':
            sug.append(((r, c-1), 'W'))
        else:
            sug.append((None, 'W'))
        if g[(r, c+1)] == '.' and g[(r-1, c+1)] == '.' and g[(r+1, c+1)] == '.':
            sug.append(((r, c+1), 'E'))
        else:
            sug.append((None, 'E'))
        sug.rotate(-(i%4))
        for k, d in sug:
            if k != None:
                suggestions[(r,c)] = k
                break

    if len(suggestions) == 0:
        print(i+1)
        exit()
        
        
    counter = defaultdict(int)

    for destination in suggestions.values():
        counter[destination] += 1
    for elf in suggestions.keys():
        suggestion = suggestions[elf]
        if counter[suggestion] == 1:
            g[suggestion] = '#'
            g[elf] = '.'

    # for tr in range(-10, 10):
    #     s = ""
    #     for tc in range(-10, 10):
    #         s+=g[(tr, tc)]
    #     print(s)


for tr, tc in g.keys():
    if g[(tr, tc)] == '#':
        min_r = min(tr, min_r)
        max_r = max(tr, max_r)
        min_c = min(tc, min_c)
        max_c = max(tc, max_c)
ca = 0



for tr in range(min_r, max_r+1):
    s = ""
    for tc in range(min_c, max_c+1):
        s+=g[(tr, tc)]
        if g[(tr, tc)] == '.':
            ca+=1
    print(s)

print('ANS', ca)

