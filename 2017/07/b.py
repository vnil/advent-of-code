from collections import Counter
from collections import defaultdict

content = open('input', 'r').readlines()
content = [c.strip() for c in content]
d = {}

for p in content:
    part1 = part2 = None
    if '->' in p:
        part1, part2 = p.split('->')
    else:
        part1 = p.strip()
    weight = int(part1.split('(')[1].strip()[:-1].strip())
    name = part1.split()[0]
    children = [a.strip() for a in part2.split(', ')] if part2 else []
    d[name] = (weight, children)


def validate():
    for a in d.keys():
        scores = []
        for c in d[a][1]:
            scores.append(calcScore(c, 0))
        counter = Counter(scores)
        if len(counter) > 1:
            return False
    return True


def calcScore(a, score):
    if len(d[a][1]) == 0:
        return score + d[a][0]
    return sum([calcScore(r, score) for r in d[a][1]]) + d[a][0]


for a in d.keys():
    scores = defaultdict(list)
    for c in d[a][1]:
        score = calcScore(c, 0)
        scores[score].append(c)
    if len(scores) > 1:
        good = wrong = 0
        bad_guy = None
        for val, s in scores.items():
            if len(s) == 1:
                wrong = val  # 22
                bad_guy = s[0]
            else:
                good = val  # 30
        diff = good - wrong
        oldWeight, deps = d[bad_guy]
        d[bad_guy] = (oldWeight + diff, deps)
        if validate():
            print(oldWeight + diff, ':::')
            exit()
        d[bad_guy] = (oldWeight, deps)
        print(diff)
# 7:40
