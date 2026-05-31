n = int(input())
nums = [str(x) for x in range(1, n+1) if x % 3 == 0]

if not nums:
    print("BO'SH")
else:
    print(' '.join(nums))