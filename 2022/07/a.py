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

g = defaultdict(set) # key: (dir, filesize)
d = list()
sizes = dict()
dirs = set(['/'])

def full_path(path, filename):
    if len(filename) > 0:
        return '/'.join(path + [filename])
    else:
        return '/'.join(path)

for row in content:
    if row[0] == '$':

        # Command
        cmd = row[2:]

        # cd
        if cmd[0:2] == "cd":
            left, target = cmd.split()
            if target == "..":
                d.pop()
            elif target == "/":
                d = ['/']
            else:
                g[full_path(d, '')].add(target)
                d.append(target)
                dirs.add(full_path(d, ''))

        
    else:
        left, right = row.split()
        if left == "dir":
            g[full_path(d, '')].add(right)
            pass
        else:
            size = int(left)
            filename = right
            g[full_path(d, '')].add(filename)
            sizes[full_path(d, filename)] = size

# populate sizes
def populate_size(file, path):
    full = full_path(path, file)
    print(full)
    if full in sizes:
        return sizes[full]
    path.append(file)
    size = sum([populate_size(a, path) for a in list(g[full_path(path, '')])])
    path.pop()
    sizes[full] = size
    return size


populate_size('/', [])
summa = 0
a = []

diff = 70000000 - sizes['/']
diff = 30000000 - diff

for dirr in list(dirs):
    if sizes[dirr] >= diff:
        a.append(sizes[dirr])
    if sizes[dirr] <= 100000:
        summa += sizes[dirr]

print(sorted(a)[0])
