from collections import defaultdict
content = open('input', 'r').readlines()
content = [c.strip() for c in content]


for row in content:
    s = 0
    points = 0
    nest = 0
    ignore_next = False
    garbage = False
    for ch in row:
        if garbage:
            s += 1
        if ignore_next:
            s -= 1
            ignore_next = False
            continue
        if ch == '<':
            if not garbage:
                s -= 1
            garbage = True
        if ch == '>':
            garbage = False
        if ch == '{' and not garbage:
            nest += 1
            points += nest
        if ch == '}' and not garbage:
            nest -= 1
        if ch == '!':
            s -= 1
            ignore_next = True
    print(points, s)
