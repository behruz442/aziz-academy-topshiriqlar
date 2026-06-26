nums = list(map(int, input().split()))

positives = [x for x in nums if x > 0]

if not positives:
    print("BO'SH")
else:
    print(' '.join(map(str, positives)))