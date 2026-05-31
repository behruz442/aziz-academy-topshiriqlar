a, b, c = input().split()
try:
    c = float(c)
except:
    pass
t = (int(a), int(b) if b.isdigit() else b, c)

print(t)