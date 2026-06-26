a = list(map(int, input().split()))

print(sum(x % 2 == 0 for x in a))
print(sum(x % 2 != 0 for x in a))