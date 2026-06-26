n = int(input())
nums = list(map(int, input().split()))
avg = sum(nums) / n
count = 0
for x in nums:
    if x > avg:
        count += 1
print(count)