n = int(input())
d = dict(input().split() for _ in range(n))
result = {k: int(v)**2 for k, v in d.items()}
print(result)