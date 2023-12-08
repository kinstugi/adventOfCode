from collections import defaultdict
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

d = 0
cur = 'AAA'
i = 0
while cur != 'ZZZ':
    if dxn[i] == 'R':
        cur = graph[cur][1]
    else:
        cur = graph[cur][0]
    d += 1
    i = (i + 1) % len(dxn)

print(d)