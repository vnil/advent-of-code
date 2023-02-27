# Take time to read
# Consider different approaches
# +-1 errors?
# Got last item?


from collections import Counter
from collections import defaultdict, deque
from pprint import pprint as pp
from itertools import combinations
from copy import deepcopy


M = 'CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF'
content = open('input', 'r').readlines()
content = [c.strip() for c in content]

s = ''
arr = []
for c in M:
    print(c)
    if len(s) > 0 and c.isupper():
        arr.append(s)
        s = c
    else:
        s += c
if len(s) > 0:
    arr.append(s)

d = {}
tran = []
for row in content:
    a, b = row.split(' => ')
    tran.append((a, b))

s = set()
for source, target in tran:
    for i, m in enumerate(arr):
        if m == source:
            cpy = arr[:]
            del cpy[i]
            cpy.insert(i, target)
            s.add(''.join(cpy))
print(len(s), super)
