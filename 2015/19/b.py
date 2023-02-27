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
# M = 'HOHOHO'
content = open('input', 'r').readlines()
content = [c.strip() for c in content]

d = defaultdict(list)
tran = []
for row in content:
    a, b = row.split(' => ')
    d[a].append(b)
print(d)

q = deque([('e', 0)])
s = set()
k = 0
while q:
    k += 1

    item, times = q.popleft()
    if k % 10000 == 0:
        print(k, item)
    if item in s or len(item) > len(M):
        continue
    s.add(item)
    if item == M:
        print('DONE', times)
        exit()
    for key, val in d.items():
        for value in val:
            cpy = item.replace(key, value, 1)
            if cpy != item:
                q.append((cpy, times+1))
