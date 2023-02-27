import collections

file_content = open('input', 'r').readlines()
cols = 50
rows = 6

grid = [[0 for _ in range(cols)] for _ in range(rows)]

for instruction in file_content:
    action = instruction.split()[:1][0]
    if action == 'rect':
        x, y = map(int, instruction.split()[1:][0].split('x'))
        for row in range(y):
            for col in range(x):
                grid[row][col] = 1
    if action == 'rotate':
        parts = instruction.split()[1:]
        dir = parts[0]
        target = int(parts[1][2:])
        steps = int(parts[3])

        if dir == 'column':
            new_col = []
            for i in range(rows):
                new_col.append(grid[(i+rows-steps) % rows][target])
            for i in range(rows):
                grid[i][target] = new_col[i]
        else:
            new_row = []
            for i in range(cols):
                new_row.append(grid[target][(i+cols-steps) % cols])
            for i in range(cols):
                grid[target][i] = new_row[i]


for a in grid:
    s = ''
    for c in a:
        if c == 1:
            s += '#'
        else:
            s += '.'
    print(s)


s = 0
for k in grid:
    s += sum(k)
print(s)
