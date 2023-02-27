obj = {}

facit = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}


for line in open('./day15.txt').readlines():
    sue, *rest = line.strip().split(': ')
    sue = sue[4:]
    o = {}
    s = ': '.join(rest)

    for row in s.split(', '):
        k, v = row.split(': ')
        o[k] = int(v)
    obj[sue] = o

for k, v in obj.items():
    bad = False
    for prop_key, prop_value in v.items():
        if prop_key in ['cats', 'trees']:
            if facit[prop_key] >= prop_value:
                bad = True
        elif prop_key in ['pomeranians', 'goldfish']:
            if facit[prop_key] <= prop_value:
                bad = True
        else:
            if facit[prop_key] != prop_value:
                bad = True
#    for prop_key, prop_value in v.items():
#        if facit[prop_key] != prop_value:
#            bad = True

    if not bad:
        print(k)
