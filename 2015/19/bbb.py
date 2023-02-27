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

d = defaultdict(list)
for row in content:
    source, target = row.split(' => ')
    d[source].append(target)

available_replacements = d.keys()

q = deque([('e', 0)])
visited = dict()
i = 0
mina = 99999
while q:
    i+=1

    item, steps = q.pop()
    if item == M:
        print('ANS', steps)
        mina = min(mina, steps)

    if i%1000000==0:
        print(len(q), i, steps, item)
    if len(item) > len(M):
        #print(debug)
        continue
    # if e in item and len > 1, abort
    if item in visited and visited[item] <= steps:
        continue
    visited[item] = steps
    
        #break
    for rep in available_replacements:
        
        p = 0
        while True:
            index = item.find(rep, p)
            if index == -1:
                break
            
            for ver in d[rep]:
                alt = item[:p] + item[p:].replace(rep, ver, 1)
                q.append((alt, steps+1))
            p=index+1
            
            
            
print(mina, i)

