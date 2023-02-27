content = open('ex', 'r').readlines()
content = [c.strip() for c in content]
d = {}

for p in content:
    part1 = part2 = None
    if '->' in p:
        part1, part2 = p.split('->')
    else:
        part1 = p.strip()

    weight = part1.split('(')[1].strip()[:-1]
    name = part1.split()[0]
    children = [a.strip() for a in part2.split(', ')] if part2 else []
    d[name] = (weight, children)

for a in d.keys():
    found = False
    for b in d.values():
        if a in b:
            found = True
    if not found:
        print(a)
# 7:40
