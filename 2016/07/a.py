file_content = open('input', 'r').readlines()
count = 0
for row in file_content:
    inside = False
    found = False
    for i in range(len(row)-3):
        c = row[i]
        if c == '[':
            inside = True
            continue
        elif c == ']':
            inside = False
            continue
        if not found and not inside and row[i+1] == row[i+2] and row[i] == row[i+3] and row[i] != row[i+1]:
            count += 1
            found = True
        elif inside and row[i+1] == row[i+2] and row[i] == row[i+3] and row[i] != row[i+1]:
            if found:
                count -= 1
            break

print(count)
