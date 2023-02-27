from collections import defaultdict
content = open('input', 'r').readlines()
content = [c.strip() for c in content]


d = defaultdict(int)
maxa = 0
for row in content:
    row.replace('- ', '-')
    print(row)
    a, b, c, dd, e, f, g = row.split()
    diff = 0
    if b == 'inc':
        diff = int(c)
    else:
        diff = -int(c)
    check_val = d[e]
    val = int(g)
    if f == '>' and check_val > val:
        d[a] += diff
    if f == '!=' and check_val != val:
        d[a] += diff
    if f == '<' and check_val < val:
        d[a] += diff
    if f == '>=' and check_val >= val:
        d[a] += diff
    if f == '<=' and check_val <= val:
        d[a] += diff
    if f == '==' and check_val == val:
        d[a] += diff
    maxa = max(maxa, d[a])

print(sorted(d.items(), key=lambda x: x[1])[-1])
print(maxa)
