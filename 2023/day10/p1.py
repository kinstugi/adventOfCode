from collections import deque

grid = []
left,right,up,down = (0,-1), (0, 1), (-1, 0), (1, 0)
dxn_mp = {
    'J': [up, left], 'F': [up, down, right], '7': [up, down, left], 'L': [up, down, right],
    '-': [right, left], '|': [up, down]
}
start_x, start_y = 0, 0

with open('data.in') as fh:
    r = 0
    for line in fh:
        line = line.strip()
        grid.append(list(line))
        for i, ch in enumerate(line):
            if ch == 'S':
                start_x, start_y = r, i
        r += 1

def bfs(x, y, graph):
    d_mp  = [[-999 for _ in range(len(graph[0]))] for _ in range(len(graph))]

    q = deque([(x, y)])
    seen = set()
    d = 0
    while q:
        cnt = len(q)
        for _ in range(cnt):
            r,c = q.popleft()
            if r < 0 or c < 0 or r >= len(graph) or c >= len(graph[0]) or (r,c) in seen: 
                continue

            d_mp[r][c] = d
            seen.add((r,c))

            if graph[r][c] == 'J':
                q.append((r-1,c))
                q.append((r,c-1))
            elif graph[r][c] == 'F':
                q.append((r,c+1))
                q.append((r+1,c))
            elif graph[r][c] == '7':
                q.append((r+1,c))
                q.append((r,c-1))
            elif graph[r][c] == 'L':
                q.append((r-1,c))
                q.append((r,c+1))
            elif graph[r][c] == '-':
                q.append((r,c+1))
                q.append((r,c-1))
            elif graph[r][c] == '|':
                q.append((r-1,c))
                q.append((r+1,c))
            elif graph[r][c] == 'S':
                pass
            else:
                d_mp[r][c] = -1
                continue
        d += 1

    ans = 0
    for nn in d_mp:
        ans = max(ans, max(nn))
    print(ans)
    #print(d_mp)

grid[start_x][start_y] = '7'
bfs(start_x, start_y, grid)
    