
from functools import cache


@cache
def helper(txt, nums):
    if txt == "":
        return 1 if not nums else 0
    if not nums:
        return 0 if "#" in txt else 1
    res = 0
    if txt[0] in ".?":
        res += helper(txt[1:], nums)

    if txt[0] in "#?":
        if nums[0] <= len(txt) and '.' not in  txt[:nums[0]] and (len(txt) == nums[0] or '#' != txt[nums[0]]):
            res += helper(txt[nums[0]+1:], nums[1:])
    return res

tot = 0
with open('data.in') as fh:
    for line in fh:
        a,b = line.strip().split()
        b = tuple(map(int, b.split(',')))
        a = "?".join([a] * 5)
        b *= 5
        tot += helper(a, b)

print(tot)