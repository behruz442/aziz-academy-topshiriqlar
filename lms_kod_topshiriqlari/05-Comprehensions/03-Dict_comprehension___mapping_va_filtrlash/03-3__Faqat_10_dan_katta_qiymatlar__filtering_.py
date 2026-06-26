n = int(input())
d = {k: int(v) for k, v in (input().split() for _ in range(n))}
res = {k: v for k, v in d.items() if v > 10}
print(res)