import sys

sys.setrecursionlimit(20000)
data = open('a_input.in').read().strip().split('\n')

R,C = len(data) , len(data[0])

# grid = [list(item) for item in data]
dxn = ((0,1), (0,-1), (1,0), (-1,0))

seen = set()
def propagate(r,c, d=0, grid=[]):
    if r < 0 or c < 0 or r >= R or c >= C: return
    if (r,c,d) in seen: return 
    #todo check for visited shit
    cell = data[r][c]
    seen.add((r,c,d))
    grid[r][c] = '#'
    
    if cell == '.':
        propagate(r+dxn[d][0], c+dxn[d][1], d, grid)
    elif cell == '|':
        if d == 0 or d == 1:
            propagate(r-1,c, 3, grid)
            propagate(r+1,c, 2, grid)
        else:
            propagate(r+dxn[d][0], c+dxn[d][1], d, grid)
    elif cell == '-':
        if d == 3 or d == 2:
            propagate(r,c-1, 1, grid)
            propagate(r,c+1, 0, grid)
        else:
            propagate(r+dxn[d][0], c+dxn[d][1], d, grid)
    elif cell == '\\':
        if d == 0:
            propagate(r+1,c, 2, grid)
        elif d == 1:
            propagate(r-1,c, 3, grid)
        elif d == 2:
            propagate(r,c+1, 0, grid)
        else:
            propagate(r,c-1, 1, grid)
    elif cell == '/':
        if d == 0:
            propagate(r-1,c, 3, grid)
        elif d == 1:
            propagate(r+1,c, 2, grid)
        elif d == 2:
            propagate(r,c-1, 1, grid)
        else:
            propagate(r,c+1, 0, grid)

def count(r,c, d):
    seen.clear()
    grid = [list(item) for item in data]
    propagate(r,c, d, grid)
    ans = 0
    for row in grid:
        for col in row:
            if col == '#':
                ans += 1
    return ans

total = 0
#part one
print("part1 ",count(0, 0, 0))


# part two
for r in range(R):
    total = max(total, count(r, 0, 0), count(r, 0, 2), count(r, 0, 3), count(r, 0, 1))
    total = max(total, count(r, C-1, 0), count(r, C-1, 2), count(r, C-1, 3), count(r, C-1, 1))

for c in range(C):
    total = max(total, count(0, c, 0), count(0, c, 2), count(0, c, 3), count(0, c, 1))
    total = max(total, count(R-1, c, 0), count(R-1, c, 2), count(R-1, c, 3), count(R-1,c, 1)) 
print("part2 ",total)