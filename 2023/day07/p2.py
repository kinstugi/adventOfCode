from collections import Counter

weight = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10}
for i in range(2, 10):
    weight[str(i)] = i


def fix(dd:dict):
    ch, cnt = '', 0
    for k,v in dd.items():
        if cnt < v and k != 'J':
            cnt = v
            ch = k
    dd[ch] += dd.get('J', 0)
    if 'J' in dd:
        del dd['J']

def grade(dd:dict)->int:
    ll = list(dd.values())
    ll.sort()
    if [5] == ll:
        return 7
    elif [1,4] == ll:
        return 6
    elif [2,3] == ll:
        return 5
    elif [1,1,3] == ll:
        return 4
    elif [1,2,2] == ll:
        return 3
    elif [1,1,1,2] == ll:
        return 2
    return 1

arr = []

with open('data.in') as fh:
    for line in fh:
        line = line.strip().split()
        nrr = [weight[c] for c in line[0]]
        cntr = Counter(line[0])
        fix(cntr)
        
        arr.append((grade(cntr), nrr, line[0], int(line[1])))

arr.sort()
ans = 0

for i in range(len(arr)):
    ans += arr[i][-1] * (i+1)

print(ans)
