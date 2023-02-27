

# Take time to read
# Consider different approaches
# +-1 errors?
# Got last item?
# What is the diff between states? Pattern?


from collections import Counter
from collections import defaultdict, deque
from pprint import pprint as pp
from itertools import combinations
from copy import deepcopy
import math
import re
from queue import PriorityQueue

content = open('i', 'r').readlines()
content = [c.strip() for c in content][0]



m = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

m3 = {
    '000': '0',
    '001': '1',
    '010': '2',
    '011': '3',
    '100': '4',
    '101': '5',
    '110': '6',
    '111': '7',
}

main_bin = ''

for c in content:
    main_bin += m[c]
p = 0

total_versions = 0
def literal(bin):
    global p
    p += 6
    val = ''
    while True:
        sub = ''.join(bin[p+1:p+5])
        val+=sub
        if bin[p] == '0':
            break
        p+=5
    p+=5
    return int(val,2)

def operator(bin, type_id):
    global p

    length_id = bin[p+6]
    p+=7

    arr = []

    if length_id == '0':
        total_length = int(''.join(bin[p:p+15]), 2)

        p+=15
        start_read = p
        while p < start_read + total_length:
            arr.append(parse_packet(bin))
    else:
        total_packets = int(''.join(bin[p:p+11]), 2)
        p+=11
        for _ in range(total_packets):
            arr.append(parse_packet(bin))

    if type_id == 0:
        return sum(arr)
    if type_id == 1:
        if len(arr) == 1:
            return arr[0]
        q = 1
        for a in arr:
            q*=a
        return q
    if type_id == 2:
        return min(arr)
    if type_id == 3:
        return max(arr)
    if type_id == 5:
        return 1 if arr[0] > arr[1] else 0
    if type_id == 6:
        return 1 if arr[0] < arr[1] else 0
    if type_id == 7:
        return 1 if arr[0] == arr[1] else 0

def parse_packet(bin):
    global p
    global total_versions

    version = int(''.join(bin[p:p+3]), 2)
    type_id = int(''.join(bin[p+3:p+6]), 2)
    total_versions += int(version)

    if type_id == 4:
        return literal(bin)
    else:
        return operator(bin, type_id)

part2 = parse_packet(main_bin)
print('part1', total_versions)
print('part2', part2)

