s = {w.lower() for w in input().split() if w. isalpha()}
print(*sorted(s) if s else ["BO'SH"])