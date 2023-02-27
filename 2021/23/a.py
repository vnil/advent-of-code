

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

content = open('e', 'r').readlines()
grid = [c.strip() for c in content]

amps = []

cost = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}

HC = {
    'A': 3,
    'B': 5,
    'C': 7,
    'D': 9
}

class Amphipods:
    def __init__(self, letter, state, r, c):
        self.letter = letter
        self.state = state
        self.r = r
        self.c = c
        self.move_count = 0
    def __str__(self):
        return self.letter + ',' + self.state + ',' + str(self.r) + ',' + str(self.c)

hallway = [None for _ in range(13)]


def can_go_home(amp):
    home_column = HC[amp.letter]
    first_row = grid[2][home_column]
    second_row = grid[3][home_column]
    return (first_row == '.' or first_row == amp.letter) and (second_row == '.' or second_row == amp.letter)
        
def move_home(amp):
    home_column = HC[amp.letter]
    first_row = grid[2][home_column]
    second_row = grid[3][home_column]

    grid[3][home_column] = amp.letter
    dc = abs(amp.c - home_column)
    dr = None
    if second_row == '.':    
        dr = 2
    else:
        dr = 1
    amp.move_count += dr + dc
    amp.r = dr + 1
    amp.c = home_column


for r,row in enumerate(content):
    for c, char in enumerate(row):
        if char == 'A' or char == 'B' or char == 'C' or char == 'D':
            amp = Amphipods(char, 'stuck' if r == 3 else 'available', r, c)
            amps.append(amp)

def one_round(amps):
    new_hallway = [None for _ in range(13)]
    for i, amp in enumerate(hallway):
        if can_go_home(amp):
            move_home(amp)
    for amp in amps:
        print(amp)