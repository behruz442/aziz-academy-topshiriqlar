words = [w.lower() for w in input().split()]

s = {(w, len(w)) for w in words}
s = sorted(s)

print(len(s))
for w, i in s:
    print(f"{w}:{i}")