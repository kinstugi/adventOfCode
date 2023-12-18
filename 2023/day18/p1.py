dxns = {'D': (1, 0), 'U': (-1, 0), 'R': (0, 1), 'L': (0, -1)}
points = [(0, 0)]
b = 0
with open('b_input.in') as fh:
    for line in fh:
        d, cnt, color = line.strip().split()
        cnt = int(cnt)
        b += cnt
        r,c = points[-1]
        dr,dc = dxns[d]
        points.append((r + cnt*dr, c + cnt*dc))

A = abs(sum([points[i][0] * (points[i-1][1] - points[(i+1) % len(points)][1]) for i in range(len(points))])) // 2
i = A - b // 2 + 1
print(i + b)