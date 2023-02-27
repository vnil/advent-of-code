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

content = open('i', 'r').readlines()
grid = [a[0:-1] for a in content]

cart_list = ['^', '>', 'v', '<']
cart_dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

valid_carts = set(cart_list)
carts = defaultdict(int)


def create_empty_track():
    cpy = [list(s) for s in grid]

    for y in range(len(cpy)):
        for x in range(len(cpy[y])):
            if cpy[y][x] in valid_carts:
                c = cpy[y][x]
                if c == '^' or c == 'v':
                    cpy[y][x] = '|'
                else:
                    cpy[y][x] = '-'
    return cpy


empty_track = create_empty_track()


for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] in valid_carts:
            carts[(y, x)] = (2, cart_list.index(grid[y][x]))


def print_grid(grid):
    for row in grid:
        print(''.join(row))


def print_grid_delux(grid, carts):
    for y, row in enumerate(grid):
        s = ''
        for x, c in enumerate(row):
            if (y, x) in carts:
                s += '#'
            else:
                s += grid[y][x]
        print(s)
    print()


current_carts = sorted(list(carts.keys()), key=lambda x: (x[0], x[1]))

while True:
    current_carts = sorted(list(carts.keys()), key=lambda x: (x[0], x[1]))
    #print_grid_delux(empty_track, carts)
    if len(carts) <= 1:
        fy, fx = list(carts.keys())[0]
        print('Last cart at:', fx, fy)
        exit()
    for (y, x) in current_carts:
        if (y, x) not in carts:
            continue
        rot, dir_index = carts[(y, x)]
        del carts[(y, x)]
        dy, dx = cart_dirs[dir_index]
        next_y = dy + y
        next_x = dx + x
        if (next_y, next_x) in carts:
            print('Crash at', next_x, next_y)
            del carts[(next_y, next_x)]
            continue

        grid_char = empty_track[next_y][next_x]
        if grid_char == '-' or grid_char == '|':
            carts[(next_y, next_x)] = (rot, dir_index)

        elif grid_char == '+':
            new_rot = (rot + 1) % 3
            new_dir_index = (dir_index + new_rot - 1 + 4) % 4
            carts[(next_y, next_x)] = (new_rot, new_dir_index)
        elif grid_char == '/' or grid_char == '\\':
            delta = 0
            if grid_char == '/':
                delta = 1 if dir_index == 2 or dir_index == 0 else -1
            else:
                delta = 1 if dir_index == 1 or dir_index == 3 else -1
            new_dir_index = (dir_index + delta + 4) % 4
            carts[(next_y, next_x)] = (rot, new_dir_index)
