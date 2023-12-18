import heapq

data = open('a_input.in').read().strip().splitlines()
data = [[int(c) for c in row] for row in data]

R, C = len(data), len(data[0])
right, left, up, down = 0, 1, 2, 3

def outta_bounds(r:int, c:int)->bool:
    if r < 0 or c < 0 or r >= R or c >= C: return True
    return False

#
def solve(x, y, dis, dxn):
    seen = [[float('inf') for c in range(C)] for r in range(R)]
    seen[x][y] = 0

    pq = [(dis, x, y, dxn, 2)]
    heapq.heapify(pq)

    while pq:
        d, r, c, dr, s = heapq.heappop(pq)
        
        if dr == right or dr == left:
            if not outta_bounds(r-1, c) and d + data[r-1][c] < seen[r-1][c]:
                seen[r-1][c] = d + data[r-1][c]
                heapq.heappush(pq,(d + data[r-1][c], r-1, c, up, 2))
            if not outta_bounds(r+1, c) and d + data[r+1][c] < seen[r+1][c]:
                seen[r+1][c] = d + data[r+1][c]
                heapq.heappush(pq,(d + data[r+1][c], r+1, c, down, 2))
            if dr == right and not outta_bounds(r, c+1) and d + data[r][c+1] < seen[r][c+1] and s > 0:
                seen[r][c+1] = d + data[r][c+1]
                heapq.heappush(pq,(d+data[r][c+1], r, c+1, right, s-1))
            elif dr == left and not outta_bounds(r, c-1) and d+data[r][c-1] < seen[r][c-1] and s > 0:
                seen[r][c-1] = d + data[r][c-1]
                heapq.heappush(pq, (d + data[r][c-1], r, c-1, left, s-1))
        else:
            if not outta_bounds(r, c-1) and d + data[r][c-1] < seen[r][c-1]:
                seen[r][c-1] = d + data[r][c-1]
                heapq.heappush(pq,(d + data[r][c-1], r, c-1, left, 2))
            if not outta_bounds(r, c+1) and d + data[r][c+1] < seen[r][c+1]:
                seen[r][c+1] = d + data[r][c+1]
                heapq.heappush(pq,(d + data[r][c+1], r, c+1, right, 2))

            if dr == up and not outta_bounds(r-1, c) and d + data[r-1][c] < seen[r-1][c] and s > 0:
                seen[r-1][c] = d + data[r-1][c]
                heapq.heappush(pq,(d + data[r-1][c], r-1, c, up, s-1))
            elif dr == down and not outta_bounds(r+1, c) and d + data[r+1][c] < seen[r+1][c] and s > 0:
                seen[r+1][c] = d + data[r+1][c]
                heapq.heappush(pq,(d + data[r+1][c], r+1, c, down, s-1))

    return seen[R-1][C-1] 
        
a = solve(0, 0, 0, right)
b = solve(0, 0, 0, down)
print(a, b, " <<<< ")