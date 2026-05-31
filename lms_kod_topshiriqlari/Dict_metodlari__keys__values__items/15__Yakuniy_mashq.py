s = [input().split() for _ in range(3)]
m = max(s, key = lambda x: int(x[1]))
print(m[0], m[1])