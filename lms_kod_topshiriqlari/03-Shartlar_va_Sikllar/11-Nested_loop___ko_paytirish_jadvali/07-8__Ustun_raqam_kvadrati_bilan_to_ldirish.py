n,m = map(int, input().split())
for j in range(n, m+1):
    print((1*j) ** 2, end= ' ' if j < m else '')