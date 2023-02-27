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
import time
start_time = time.time()

content = open('mod2', 'r').readlines()
content = [c.strip() for c in content]

G = defaultdict(list)


data = [0, 0, 0, 0]
data_index_mapper = {
    'w': 0,
    'x': 1,
    'y': 2,
    'z': 3
}


def test_nr(nrstring, get_actual_nr = False):
    actual_nr = ''
    p = 0
    data = [0, 0, 0, 0]
    for row in content:
        inst, left, right = row.split(' ')

        if inst == 'vik': #manually added instruction to make w == x when possible
            if 1 <= data[1] <= 9:
                data[0] = data[1]
            actual_nr += str(data[0])

            continue

        is_digit = right.replace('-', '').isdigit()
        if is_digit:
            right = int(right)
        var_index = data_index_mapper[left]
        if inst == 'inp':
            if p >= len(nrstring):
                return data
            data[var_index] = int(nrstring[p])
            p+=1
        elif inst == 'add':
            data[var_index] += right if is_digit else data[data_index_mapper[right]]
        elif inst == 'mul':
            data[var_index] *= right if is_digit else data[data_index_mapper[right]]
        elif inst == 'div':
            data[var_index] = data[var_index] // (right if is_digit else data[data_index_mapper[right]])
        elif inst == 'mod':
            data[var_index] = data[var_index] % (right if is_digit else data[data_index_mapper[right]])
        elif inst == 'eql':
            if data[var_index] == (right if is_digit else data[data_index_mapper[right]]):
                data[var_index] = 1
            else:
                data[var_index] = 0
        else:
            assert False
    if get_actual_nr:
        return actual_nr
    return data


# used to find largest and smallest with placeholders
def part1():
    for a in range(9999, 1000, -1):
        s = str(a)
        if '0' in s:
            continue
        s+='99'
        for b in range(99, 10, -1):
            bs = str(b)
            if '0' in bs:
                continue
            ss = s + bs + '99'
            for c in range(9, 0, -1):
                cs = str(c)
                sss = ss + cs + '999'
                
                e = test_nr(sss)
                if e[3] == 0:
                    return sss

def part2():
    for a in range(1111, 10000):
        s = str(a)
        if '0' in s:
            continue
        s+='11'
        for b in range(11, 100):
            bs = str(b)
            if '0' in bs:
                continue
            ss = s + bs + '11'
            for c in range(1, 10):
                cs = str(c)
                sss = ss + cs + '111'
                
                e = test_nr(sss)
                if e[3] == 0:
                    return sss
print(test_nr(part1(), True))
print(test_nr(part2(), True))