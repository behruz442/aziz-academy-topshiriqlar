a = list(map(int, input().split()))

d = {}

for x in a:
    d[x] = d.get(x, 0) + 1
    
print(min(d, key=lambda x: (-d[x], x)))