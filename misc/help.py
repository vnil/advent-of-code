R = len(grid)
C = len(grid)

D = [(-1, 0), (0, 1), (1, 0), (0, -1)]

visited = set()

for qr in range(R):
    for qc in range(C):
        #if grid[r][c] != '.':
        #    continue

        queue = deque([(qr, qc)])
        while queue:
            r, c = queue.pop()
            if (r, c) in visited:
                continue
            visited.add((r, c))

            #if grid[r][c] != '.':
            #    continue

            for dr, dc in D:
                ar = r + dr
                ac = c + dc
                queue.append((ar, ac))



grid = [[0, 0, 0],[0, 1, 0],[0, 0, 0]]

R = len(grid)
C = len(grid)

D = [(-1, 0), (0, 1), (1, 0), (0, -1)]         

for _ in range(3):
    grid_copy = deepcopy(grid)
    for r in range(R):
        for c in range(C):
            #variables for r-c
            count = 0
            for dr, dc in D:
                ar = r + dr
                ac = c + dc
                if 0 <= ar < R and 0 <= ac < C:
                    if grid[ar][ac] == 1:
                        count+=1
            grid_copy[r][c] = count
    grid = grid_copy
pp(grid)  