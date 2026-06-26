nums = list(map(int, input().split()))

result = [x for x in nums if x > 10]

if not result:
    print("BO'SH")
else:
    print(' '.join(map(str, result)))