data = []
with open('data.in') as fh:
    for line in fh:
        nn = line.split(':')[1].strip().split()
        nn = "".join(nn)
        data.append(int(nn))

def calc(t, dis):
    lo, hi = 0, t
    lb, rb = -1, -1
    while lo <= hi:
        m = (lo + hi) // 2

        if m * (t - m) > dis:
            hi = m - 1
            lb = m
        else:
            lo = m + 1

    lo, hi = 0, t

    while lo <= hi:
        m = (lo + hi) // 2
        if m * (t - m) > dis:
            lo = m + 1
            rb = m
        else:
            hi = m - 1
    return rb - lb + 1

print(calc(data[0], data[1]))