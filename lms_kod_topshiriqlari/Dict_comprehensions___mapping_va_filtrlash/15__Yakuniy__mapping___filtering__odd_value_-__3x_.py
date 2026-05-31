n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    v = int(v)
    
    if abs(v) >= 2:
        d[k] = v * 3 if v % 2 else v * 2
        
print(d)