n = int(input())
res = {k:int(v) for k, v in (input().split() for _ in range(n)) if k.startswith('a')}
print(res)