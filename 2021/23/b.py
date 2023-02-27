

# Take time to read
# Consider different approaches
# +-1 errors?
# Got last item?
# What is the diff between states? Pattern?


from collections import Counter
from collections import defaultdict, deque
from pprint import pprint as pp
from itertools import combinations, permutations
from copy import deepcopy
import math
import re
from queue import PriorityQueue
import json

content = open('b', 'r').readlines()
#content = [[int(x) for x in c.strip()] for c in content]
content = [[x for x in c.strip()] for c in content]


hole_depth = 4


slot_columns = [3, 5, 7, 9]
home_slot_letters = ['A', 'B', 'C', 'D']

index_mapper = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3
}

cost = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}

hallways_places = [1, 2, 4, 6, 8, 10, 11]
seen = set()

def pg(g):
    for row in g:
        print(''.join(row))
    print()
    
min_price = math.inf    
count = 0

def serialise(g):
    s = ''
    for row in g:
        s+=''.join(row)
    return s
min_path = None
def go(grid, path, price = 0):

    #ko = serialise(grid)
    #if ko in seen:
    #    return
    #seen.add(ko)
    
    global min_price
    global min_path
    global count
    count+=1
    
    if count %10000 == 1:
        print(count)

    # Generate free slots
    free_slots = [True for _ in range(4)]
    for i, col in enumerate(slot_columns):
        for row in range(2, hole_depth+2):
            if grid[row][col] != '.' and grid[row][col] != home_slot_letters[i]: # Also possible for it to contain only letters that has this as home
                free_slots[i] = False
                break

    if all(free_slots):
        ok = True
        for hallway_col in hallways_places:
            if grid[1][hallway_col] != '.':
                ok = False
                break
        if ok:
            if min_price > price:
                min_path = path
                min_price = min(min_price, price)

            return
            

    # Try send hallway amps home
    for c in range(1, 12): # hallways_places ?
        if grid[1][c] != '.':
            letter = grid[1][c]
            #can grid[1][c] go home?
            index = index_mapper[letter]
            if not free_slots[index]:
                continue
            start = min(c, slot_columns[index])
            stop = max(c, slot_columns[index]) + 1
            free = True
            for hallway_path_column in range(start, stop):
                if hallway_path_column != c and grid[1][hallway_path_column] != '.':
                    free = False
                    break
            if not free:
                continue
            mod_grid = deepcopy(grid)
            # Ok, found amp in hallway that can go home. Make it go home and explore that game state
            for place_r in range(hole_depth+1, 1, -1):
                if grid[place_r][slot_columns[index]] == '.':
                    mod_grid[place_r][slot_columns[index]] = letter
                    mod_grid[1][c] = '.'
                    additional_price = abs(slot_columns[index] - c) + place_r - 1
                    go(mod_grid, list(path) + [mod_grid], price + additional_price * cost[letter])
                    return
                    #break
                    # Potentially should exit here to avoid more duplicated runs?

    # Try to move top items out to various free hallway spots
    for i, slot_column in enumerate(slot_columns):
        if free_slots[i]:
            continue
        for row in range(2, hole_depth+2):
            letter = grid[row][slot_column]
            if letter != '.':
                index = index_mapper[letter]
                #First, lets see if we can send it home directly
                if free_slots[index]:
                    path_free = True
                    for hc in range(min(slot_column, slot_columns[index]), max(slot_column, slot_columns[index]) + 1):
                        if grid[1][hc] != '.':
                            path_free = False
                    if path_free:
                        mod_grid = deepcopy(grid)

                        for place_r in range(hole_depth+1, 1, -1):
                            if grid[place_r][slot_columns[index]] == '.':
                                mod_grid[place_r][slot_columns[index]] = letter
                                mod_grid[row][slot_column] = '.'
                                additional_price = abs(slot_columns[index] - slot_column) + place_r - 1 + row - 1
                                go(mod_grid, list(path) + [mod_grid], price + additional_price * cost[letter])
                                #break
                        #break


                #Found top amp in slot, try put it in free hallway spots
                #Left
                for hallway_column in range(slot_column, 0, -1):
                    if grid[1][hallway_column] != '.':
                        break
                    mod_grid = deepcopy(grid)
                    if hallway_column in hallways_places:
                        mod_grid = deepcopy(grid)
                        mod_grid[1][hallway_column] = letter
                        mod_grid[row][slot_column] = '.'
                        additional_price = abs(hallway_column - slot_column) + row - 1
                        go(mod_grid, list(path) + [mod_grid], price + additional_price * cost[letter])
                #Right
                for hallway_column in range(slot_column, 12):
                    if grid[1][hallway_column] != '.':
                        break
                    mod_grid = deepcopy(grid)
                    if hallway_column in hallways_places:
                        mod_grid = deepcopy(grid)
                        mod_grid[1][hallway_column] = letter
                        mod_grid[row][slot_column] = '.'
                        additional_price = abs(hallway_column - slot_column) + row - 1
                        go(mod_grid, list(path) + [mod_grid], price + additional_price * cost[letter])
                break

go(content, [])


print('START ----')
for a in min_path:
    pg(a)
print('STOP  ----')

print(min_price)


