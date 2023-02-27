from collections import Counter
from collections import defaultdict
from pprint import pprint as pp

content = open('input', 'r').readlines()
content = [c.strip() for c in content]


grid = []


def print_grid(g):
    for row in g:
        print(''.join(row))
    print('----------')


for i, row in enumerate(content):
    grid.append(list(row))
lumb_set = set()
trees_set = set()

lumb = 0
trees = 0
open_ = 0

d_trees = {}
d_lumb = {}
d_open_ = {}

for row in grid:
    for ch in row:
        if ch == '#':
            lumb += 1
        elif ch == '|':
            trees += 1
        else:
            open_ += 1
d = {(trees, lumb, open_): 0}

# part two: 219919 repets with 28 gap after a while, 1000000000-1-607 % 28 = 0 so value for 607 iteration is correct for 1000000000 iteratrion (-1 since 0 index)
for m in range(1000):
    new_grid = [[x for x in row] for row in grid]
    for row in range(len(grid)):
        for col in range(len(grid)):
            current = grid[row][col]
            trees = 0
            open_ = 0
            lumb = 0
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    if dr == 0 and dc == 0:
                        continue
                    check_row = row+dr
                    check_col = col+dc
                    if check_row >= len(grid) or check_col >= len(grid[row]) or check_row < 0 or check_col < 0:
                        continue
                    check = grid[row + dr][col + dc]
                    if check == '.':
                        open_ += 1
                    if check == '#':
                        lumb += 1
                    if check == '|':
                        trees += 1
            if current == '.' and trees >= 3:
                new_grid[row][col] = '|'
            if current == '|' and lumb >= 3:
                new_grid[row][col] = '#'
            if current == '#' and lumb >= 1 and trees >= 1:
                new_grid[row][col] = '#'
            elif current == '#':
                new_grid[row][col] = '.'
    # print_grid(new_grid)
    grid = new_grid

    trees = 0
    lumb = 0
    open_ = 0

    for row in grid:
        for ch in row:
            if ch == '#':
                lumb += 1
            elif ch == '|':
                trees += 1
            else:
                open_ += 1
    ko = (trees, lumb, open_)
    if ko in d:
        print('---', m, d[ko], m - d[ko], trees*lumb)
    d[ko] = m
