ans = 0
arr = []
with open('data.in') as fh:
    for line in fh:
        card = line.split(':')[1]
        winning_nums, my_nums = card.split('|')
        winning_nums = set(map(int, winning_nums.strip().split()))
        my_nums = set(map(int, my_nums.strip().split()))

        arr.append(len(winning_nums.intersection(my_nums)))


dp = [0] * len(arr)
for i in range(len(dp)-1, -1, -1):
    dp[i] = 1 + sum(dp[i+1: i+1+arr[i]])

print(sum(dp))
print(dp)