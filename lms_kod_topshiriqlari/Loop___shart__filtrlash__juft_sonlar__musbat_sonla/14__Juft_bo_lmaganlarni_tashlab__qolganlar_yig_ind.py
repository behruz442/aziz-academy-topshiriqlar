n = int(input())
nums = list(map(int, input().split()))
total = 0

for x in nums:
    if x%2 != 0:
        continue
    total += x
print(total)