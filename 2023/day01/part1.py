def get_num(txt:str)->int:
    f, l = -1, -1
    for ch in txt:
        if not('0' <= ch <= '9'): continue
        if f == -1:
            f = int(ch)
        l = int(ch)
    return f*10 + l

with open('data.in') as fh:
    ans = 0
    for line in fh:
        ans += get_num(line)
    print(ans)