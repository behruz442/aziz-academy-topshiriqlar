nums = map(int, input().split())

s = {x for x in nums if x % 2 == 0}

print(*sorted(s) if s else["BO'SH"])