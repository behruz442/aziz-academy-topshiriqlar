nums = list(map(int, input().split()))


odds = [x for x in nums if x % 2 != 0]

if not odds:
    print("BO'SH")
else:
    print(' '.join(map(str, odds)))