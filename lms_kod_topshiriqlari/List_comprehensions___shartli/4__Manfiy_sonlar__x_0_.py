nums = list(map(int, input().split()))

nagatives = [x for x in nums if x < 0]

if not nagatives:
    print("BO'SH")
else:
    print(' '.join(map(str, nagatives)))