data = open('data.in').read().strip().split('\n\n')
# print(len(data))

def find_mirror(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]
        mn = min(r, len(grid)-r)
        above = above[: mn]
        below = below[: mn]

        if above == below:
            return r
    return 0

total = 0
for mirror in data:
    grid = mirror.strip().split('\n')
    rows = find_mirror(grid)
    cols = find_mirror(list(zip(*grid)))

    total += rows * 100 + cols

print(total)