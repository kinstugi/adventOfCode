mp = {'one':1, 'two':2, 'three': 3, 'four':4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def fix(arr,  num):
    if arr[0] == -1:
        arr[0] = num
    arr[1] = num

def get_num(txt: str):
    rr = [-1, -1]
    i = 0
    while i < len(txt):
        if '0' <= txt[i] <= '9':
            fix(rr, int(txt[i]))
        elif txt[i] == 'o' and txt[i:i+3] == 'one':
            fix(rr, 1)
        elif txt[i] == 't':
            if txt[i:i+3] == 'two':
                fix(rr, 2)
            elif txt[i:i+5] == 'three':
                fix(rr, 3)
        elif txt[i] == 'f':
            if txt[i:i+4] == 'four':
                fix(rr, 4)
            elif txt[i:i+4] == 'five':
                fix(rr, 5)
        elif txt[i] == 's':
            if txt[i:i+3] == 'six':
                fix(rr, 6)
            elif txt[i:i+5] == 'seven':
                fix(rr, 7)
        elif txt[i] == 'e' and txt[i:i+5] == 'eight':
            fix(rr, 8)
        elif txt[i] == 'n' and txt[i:i+4] == 'nine':
            fix(rr, 9)
        i += 1

    return rr[0]*10 + rr[1]

with open('data.in') as fh:
    ans = 0
    for line in fh:
        r = get_num(line)
        ans += r
    print(ans)    