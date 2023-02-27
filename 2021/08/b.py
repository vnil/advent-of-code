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

nrs = {
    '0': set([0, 2, 3, 5, 6, 7, 8, 9]),
    '1': set([0, 4, 5, 6, 8, 9]),
    '2': set([0, 1, 2, 3, 4, 7, 8, 9]),
    '3': set([2, 3, 4, 5, 6, 8, 9]),
    '4': set([0, 2, 6, 8]),
    '5': set([0, 1, 3, 4, 5, 6, 7, 8, 9]),
    '6': set([0, 2, 3, 5, 6, 8, 9]),
}

segs = {
    '0': set([0, 1, 2, 4, 5, 6]),
    '1': set([2, 5]),
    '2': set([0, 2, 3, 4, 6]),
    '3': set([0, 2, 3, 5, 6]),
    '4': set([1, 2, 3, 5]),
    '5': set([0, 1, 3, 5, 6]),
    '6': set([0, 1, 3, 4, 5, 6]),
    '7': set([0, 2, 5]),
    '8': set([0, 1, 2, 3, 4, 5, 6]),
    '9': set([0, 1, 2, 3, 5, 6]),
}

content = open('i', 'r').readlines()
content = [c.strip() for c in content]

all_segs = list([a for a in range(7)])

full = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
tot = 0
for row in content:
    first, second = row.split(' | ')
    signal_patterns = first.split()
    digits = second.split()
    possible_5_numbers = [2, 3, 5]
    possible_6_numbers = [0, 6, 9]
    possible = [set(['a', 'b', 'c', 'd', 'e', 'f', 'g']) for _ in range(7)]

    def nr_fits(n, code):
        req_segs = segs[str(n)]
        for seg in req_segs:
            print(seg, set(code), set(possible[seg]), set(code) & set(possible[seg]), len(set(code) & set(possible[seg])))
            if len(set(code) & set(possible[seg])) == 0:
                return False
                            
        return True
            
        
    final = {}

    for s in signal_patterns:
        current_set = set(list(s))

        if len(s) == 2:
            for c in s:
                possible[0].discard(c)
                possible[1].discard(c)
                possible[3].discard(c)
                possible[4].discard(c)
                possible[6].discard(c)
            possible[2] &= current_set 
            possible[5] &= current_set
        if len(s) == 3:

            for c in s:
                possible[1].discard(c)
                possible[3].discard(c)
                possible[4].discard(c)
                possible[6].discard(c)
            possible[0] &= current_set
            possible[2] &= current_set
            possible[5] &= current_set

        if len(s) == 4:
            for c in s:
                possible[0].discard(c)
                possible[4].discard(c)
                possible[6].discard(c)
            possible[1] &= current_set
            possible[2] &= current_set
            possible[3] &= current_set
            possible[5] &= current_set
        final['0'] = list(possible[0])[0]

    five = [a for a in signal_patterns if len(a) == 5]
    five_common = set(five[0]) & set(five[1]) & set(five[2])
    aa = set(possible[3]) & five_common
    k = list(aa)[0]
    possible[3] = aa
    final['3'] = k
    final['6'] = list(five_common-possible[0]-possible[3])[0]
    possible[6] = five_common-possible[0]-possible[3]


    four = [a for a in signal_patterns if len(a) == 4]
    first_seg = set(four[0])-possible[2]-possible[3]-possible[5]
    final['1'] = list(first_seg)[0]
    possible[1] = first_seg
    
    six = [a for a in signal_patterns if len(a) == 6]
    six_common = set(six[0]) & set(six[1]) & set(six[2])
    ga = six_common-possible[0]-possible[1]-possible[3]-possible[6]
    final['5'] = list(ga)[0]
    possible[5] = ga

    final['2'] = list(possible[2] - ga)[0]
    possible[2] = possible[2] - ga
    final['4'] = list(possible[4]-possible[6])[0]
    rev = {}
    for key in final:
        rev[final[key]] = key

    ma = ''
    for nr in second.split():
        sections = ''
        for part in nr:
            sections+=rev[part]
        o = [int(a) for a in sections]
        o.sort()
        for nr_key in segs:
            if list(segs[nr_key]) == o:
                ma+=nr_key
    tot+=int(ma)
print(tot)


    

