nums = list(map(int, input().split()))

result = [str(x**2 if x % 2 == 0 else x) for x in nums]
print(' '.join(result))