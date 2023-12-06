data = []
with open('data.in') as fh:
    for line in fh:
        nn = line.split(':')[1]
        nn = list(map(int, nn.strip().split()))
        data.append(nn)

def calc(t, dis):
    cnt = 0
    for i in range(1, t):
        if (i * (t-i)) > dis:
            cnt += 1
    return cnt

ans = 1
for t,d in zip(data[0], data[1]):
    ans *= calc(t, d)

print(ans)