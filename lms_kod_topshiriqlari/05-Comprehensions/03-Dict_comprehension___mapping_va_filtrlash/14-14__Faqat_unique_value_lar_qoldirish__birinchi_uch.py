n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    v = int(v)
    if v not in d. values():
        d[k] = v
print(d)