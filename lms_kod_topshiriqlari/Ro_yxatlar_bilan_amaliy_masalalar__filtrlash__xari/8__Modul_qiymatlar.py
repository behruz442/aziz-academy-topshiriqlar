n = int(input())
lst = list(map(int, input().split()))
result = [abs(x) for x in lst]
print(result)