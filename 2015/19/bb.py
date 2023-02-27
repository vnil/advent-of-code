# Take time to read
# Consider different approaches
# +-1 errors?
# Got last item?


from collections import Counter
from collections import defaultdict, deque
from pprint import pprint as pp
from itertools import combinations
from copy import deepcopy


#M = 'CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF'
fa = open('input', 'r').read()

a = fa.split('\n\n')
content = a[0].split('\n')
M = a[1]
print(M)
content = [c.strip() for c in content]

d = dict()
for row in content:
    source, target = row.split(' => ')
    d[target] = source

available_replacements = d.keys()

q = deque([(M, 0)])
visited = dict()
i = 0
mina = 9999999999
while q:
    i+=1

    item, steps = q.pop()
    if i%1000000==0:
        print(len(q), i, steps)
    # if e in item and len > 1, abort
    if item in visited and visited[item] <= steps:
        continue
    visited[item] = steps
    if item == 'e':
        print('ANS', steps)
        mina = min(mina, steps)
        #break
    for rep in available_replacements:
        p = 0
        while True:
            index = item.find(rep, p)
            if index == -1:
                break
            alt = item[:p] + item[p:].replace(rep, d[rep], 1)
            p=index+1
            if 'ee' in alt or 'HH' in alt or 'OO' in alt or 'BB' in alt or 'AlAl' in alt or 'PP' in alt or 'NN' in alt:
                continue
            q.append((alt, steps+1))
            
print(mina)

