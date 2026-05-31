n = int(input())
res = {k: ('even' if int(v) % 2 == 0 else 'odd') for k, v in (input().split() for _ in range(n))}
print(res)