from collections import Counter

file_content = open('input', 'r').readlines()
d = []
for i in range(len(file_content[0].strip())):
    s = ''

    for row in file_content:
        s += row[i]
    d.append(s)

r = ''
for a in d:
    r += Counter(a).most_common()[-1][0]

print(r)
