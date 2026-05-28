n = int(input())
nums = list(map(int, input().split()))
evens = [x for x in nums if x % 2 == 0]
print(min(evens) if evens else "No")