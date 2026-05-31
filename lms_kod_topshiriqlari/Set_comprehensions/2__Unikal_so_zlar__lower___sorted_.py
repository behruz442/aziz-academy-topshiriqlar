words = input().split()
s = {w.lower() for w in words}
print(*sorted(s))