from collections import defaultdict
grid = []
with open('data.in') as fh:
    for line in fh:
        grid.append(line.strip()+'.')

R,C = len(grid), len(grid[0])
mp = defaultdict(list)

def check(r, c, num):
    for dr in [1,0,-1]:
        for dc in [1,0,-1]:
            nr,nc = r + dr, c + dc
            if nr < 0 or nc < 0 or nr >= R or nc >= C:
                continue
            if grid[nr][nc] == '*':
                mp[(nr,nc)].append(num)
                return True 
            
    return False

ans = 0
for r in range(R):
    start, end = -1, -1
    for c in range(C):
        if '0' <= grid[r][c] <= '9':
            if start == -1:
                start = c
            end = c
        else:
            if start == -1 or end == -1:
                continue
            
            #verify link
            for m in range(start, end + 1):
                if check(r, m, int(grid[r][start:end+1])):
                    # ans += int(grid[r][start:end+1])
                    break
            start, end = -1, -1
# print(ans)
for v in mp.values():
    if len(v) < 2: continue
    prdt = 1
    for num in v:
        prdt *= num
    ans += prdt

print(ans)
