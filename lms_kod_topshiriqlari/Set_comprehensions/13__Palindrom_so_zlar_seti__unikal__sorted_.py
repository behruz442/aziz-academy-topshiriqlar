s = {w.lower() for w in input().split() if w.lower() == w.lower()[::-1]}
print(*sorted(s) if s else ["BO'SH"])