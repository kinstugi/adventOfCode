mp = {'red': 12, 'green': 13, 'blue': 14}

def check(txt: str)->int:
    rr = {'red': 0, 'green': 0, 'blue': 0}
    for pt in txt.split(';'):
        for gg in pt.split(','):
            # print(gg)
            cnt, color = gg.strip().split()
            rr[color] = max(rr[color], int(cnt))
    ans = 1
    for k,v in rr.items():
        ans *= v
    return ans

with open('data.in') as fh:
    tot = 0
    for line in fh:
        tot += check(line.strip().split(':')[1])
    
    print(tot)