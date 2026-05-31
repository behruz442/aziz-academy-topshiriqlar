n = int(input())
s = {x for x in range(1, n + 1) if x % 3 == 0}
print(*sorted(s) if s else ["BO'SH"])