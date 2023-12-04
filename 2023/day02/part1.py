mp = {'red': 12, 'green': 13, 'blue': 14}

def check(txt: str)->bool:
    for pt in txt.split(';'):
        for gg in pt.split(','):
            # print(gg)
            cnt, color = gg.strip().split()
            if int(cnt) > mp[color]: return False
    return True

with open('data.in') as fh:
    cnt = 1
    tot = 0
    for line in fh:
        if check(line.strip().split(':')[1]):
            tot += cnt
        cnt += 1
    
    print(tot)