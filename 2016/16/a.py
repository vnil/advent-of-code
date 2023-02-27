from collections import Counter
from collections import defaultdict, deque
from pprint import pprint as pp
from itertools import combinations
from copy import deepcopy


content = open('input', 'r').readlines()
content = [c.strip() for c in content]

data = '01110110101001000'
desired_length = 272
while True:
    a = data
    b = data[::-1]
    for i in range(len(a)):

    if data >= desired_length:
        break

print(data)
