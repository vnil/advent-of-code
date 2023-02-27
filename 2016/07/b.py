file_content = open('input', 'r').readlines()
count = 0
for row in file_content:
    inside = False
    findings = set()
    for i in range(len(row)-2):
        c = row[i]
        if c == '[':
            inside = True
            continue
        elif c == ']':
            inside = False
            continue
        if row[i] == row[i+2] and row[i+1] is not row[i]:
            rev = (row[i+1] + row[i] + row[i+1], not inside)
            if rev in findings:
                count += 1
                break
            findings.add((row[i] + row[i+1] + row[i+2], inside))


print(count)
