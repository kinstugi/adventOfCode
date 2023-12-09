from collections import Counter

def predict(arr: list[int]):
    mp = Counter(arr)
    if mp.get(0, -1) == len(arr): return 0
    dif  = []
    for i in range(1, len(arr)):
        dif.append(arr[i]-arr[i-1])
    return arr[-1] + predict(dif)

ans = 0
with open('data.in') as fh:
    for line in fh:
        nums = list(map(int, line.strip().split()))
        res = predict(nums)
        ans += res

print(ans)