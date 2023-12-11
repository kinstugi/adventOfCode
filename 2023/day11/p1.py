import bisect
data = open('data.in').read().split('\n')
R,C = len(data), len(data[0])

empty_row = []
for r in range(R):
    if all([ch == '.' for ch in data[r]]):
        empty_row.append(r)

empty_col = []
for c in range(C):
    flag = True
    for r in range(R):
        if data[r][c] != '.':
            flag = False
            break
    
    if flag:
        empty_col.append(c)

galaxies = []

for r in range(R):
    for c in range(C):
        if data[r][c] == '#':
            r_c = bisect.bisect_left(empty_row, r)
            c_c = bisect.bisect_left(empty_col, c)
            galaxies.append((r + r_c, c + c_c))

ans = 0

for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        ans += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

print(ans)