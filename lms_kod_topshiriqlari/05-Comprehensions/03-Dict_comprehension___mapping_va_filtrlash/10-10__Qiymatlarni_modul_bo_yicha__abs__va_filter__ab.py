n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    av = abs(int(value))
    if av >= 5:
        d[key] = av
print(d)