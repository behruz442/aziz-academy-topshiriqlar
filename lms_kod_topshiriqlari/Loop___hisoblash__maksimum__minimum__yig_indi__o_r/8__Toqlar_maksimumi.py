n = int(input())
nums = list(map(int, input().split()))
odds = [x for x in nums if x % 2 != 0]
print(max(odds) if odds else "No")