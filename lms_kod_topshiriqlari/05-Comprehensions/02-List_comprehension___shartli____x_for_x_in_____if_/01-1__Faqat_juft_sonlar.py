nums = list(map(int, input().split()))

evens = [x for x in nums if x % 2 == 0]

if not evens:
    print("BO'SH")
else:
    print(' '.join(map(str, evens)))