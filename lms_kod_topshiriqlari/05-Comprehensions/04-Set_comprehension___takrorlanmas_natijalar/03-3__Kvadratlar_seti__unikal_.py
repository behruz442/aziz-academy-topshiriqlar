nums = map(int, input().split())
s = {x**2 for x in nums}
print(*sorted(s))