from collections import defaultdict, deque
import math
data = ""

with open('data.in') as fh:
    data = fh.read()


data = data.split('\n\n')
dxn = data[0].strip()

graph = defaultdict(list)

for line in data[1].split('\n'):
    ll = line.strip().split('=')
    graph[ll[0].strip()[:3]].append(ll[1].strip()[1:4])
    graph[ll[0].strip()[:3]].append(ll[1].strip()[6:9])

# print(graph)
# print(dxn)

def check(nd):
    d = 0
    i = 0
    cur = nd

    while cur[-1] != 'Z':
        if dxn[i] == 'L':
            cur = graph[cur][0]
        else:
            cur = graph[cur][1]
        d += 1
        i = (i + 1) % len(dxn)
    return d

arr = []
for k in graph.keys():
    if k[-1] == 'A':
        arr.append(check(k))

res = math.lcm(*arr)
print(res)