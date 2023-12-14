data = open('data.in').read().strip().split('\n\n')
# print(len(data))

def count_diff(a, b):
    cnt = 0
    for r in range(len(a)):
        for c in range(len(a[0])):
            if a[r][c] != b[r][c]:
                cnt += 1
    return cnt

def find_mirror(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]
        mn = min(r, len(grid)-r)
        
        above = above[: mn]
        below = below[: mn]
        tt= count_diff(above, below)
        if tt == 1:
            return r
    return 0

total = 0
for mirror in data:
    grid = mirror.strip().splitlines()
    rows = find_mirror(grid)
    cols = find_mirror(list(zip(*grid)))
    # print(rows, cols)
    total += rows * 100 + cols

print(total)