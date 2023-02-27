file_content = open('input', 'r').readlines()
k = file_content[0].split(', ')

dy = dx = 0

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
currentDir = 0
visited = set()

for inst in k:
    dir = inst[:1]
    dist = int(inst[1:])
    if dir == 'R':
        currentDir = (currentDir + 1) % 4
    else:
        currentDir = (currentDir + 3) % 4
    d = dirs[currentDir]
    for i in range(1, dist + 1):
        ax = dx + d[0]*i
        ay = dy + d[1]*i
        if (ax, ay) in visited:
            print(abs(ax)+abs(ay))
            exit()
        visited.add((ax, ay))
    dx += d[0]*dist
    dy += d[1]*dist
