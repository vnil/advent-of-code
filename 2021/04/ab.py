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
import re

content = open('i', 'r').readlines()
content = [c.strip() for c in content]

numbers = deque(map(int, content[0].split(',')))

content = content[2:]

bingos = []
marked = []

winners = set()


def winner_score(plate_nr, nr):
    if plate_nr in winners:
        return
    winners.add(plate_nr)

    s = []
    for r in range(len(bingos[plate_nr])):
        for c in range(len(bingos[plate_nr][r])):
            if marked[plate_nr][r][c] == False:
                s.append(bingos[plate_nr][r][c])
    if len(winners) == 1:
        print('PART 1:', sum(s) * nr)

    elif len(winners) == len(bingos):
        print('PART 2:', sum(s) * nr)


for i in range(0, len(content), 6):
    bingo = []
    for j in range(5):
        row = list(map(int, re.findall('\d+', content[i+j])))
        bingo.append(row)
    bingos.append(bingo)

    mark = []
    for _ in range(5):
        mark_row = []
        for _ in range(5):
            mark_row.append(False)
        mark.append(mark_row)
    marked.append(mark)


while numbers:
    number = numbers.popleft()
    for plate_nr, bingo in enumerate(bingos):
        for r, row in enumerate(bingo):
            for c, nr in enumerate(row):
                if nr == number:
                    marked[plate_nr][r][c] = True

    # horizontal
    for plate_nr, mark in enumerate(marked):
        for r in range(5):
            all = True
            for c in range(5):
                if mark[r][c] != True:
                    all = False
                    break
            if all:
                winner_score(plate_nr, number)

    # vertical
    for plate_nr, mark in enumerate(marked):
        for c in range(5):
            all = True
            for r in range(5):
                if mark[r][c] != True:
                    all = False
                    break
            if all:
                winner_score(plate_nr, number)
