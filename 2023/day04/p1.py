import argparse
ag = argparse.ArgumentParser()
ag.add_argument('-d', help='which data to select')

p = ag.parse_args()
ans = 0
with open('data.in') as fh:
    for line in fh:
        card = line.split(':')[1]
        winning_nums, my_nums = card.split('|')
        winning_nums = set(map(int, winning_nums.strip().split()))
        my_nums = set(map(int, my_nums.strip().split()))

        matched_nums = my_nums.intersection(winning_nums)
        if not matched_nums:
            continue
        
        ans += 2 ** (len(matched_nums)-1)

print(ans)