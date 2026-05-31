n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    d[key] = int(value)
x = int(input())

result = {}
for key, value in d.items():
    if value >= x:
        result[key] = value
        
print(result)