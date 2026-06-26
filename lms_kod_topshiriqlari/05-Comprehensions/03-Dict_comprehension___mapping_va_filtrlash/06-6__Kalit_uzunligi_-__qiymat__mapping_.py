n = int(input())
res = {len(k): int(v) for k, v in (input().split() for _ in range(n))}
print(res)