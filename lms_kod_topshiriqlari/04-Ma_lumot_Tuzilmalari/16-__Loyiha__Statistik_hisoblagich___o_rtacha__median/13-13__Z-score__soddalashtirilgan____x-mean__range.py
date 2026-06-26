a = list(map(int, input().split()))
m = sum(a) / len(a)
r = max(a) - min(a)
print(*[f"{(x-m)/r if r else 0:.2f}" for x in a])