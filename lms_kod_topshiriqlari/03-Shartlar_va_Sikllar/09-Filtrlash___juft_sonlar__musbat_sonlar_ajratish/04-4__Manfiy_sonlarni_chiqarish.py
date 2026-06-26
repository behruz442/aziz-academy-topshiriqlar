n = int(input())
sonlar = list(map(int, input().split()))

for son in sonlar:
    if son >= 0:
        continue
    print(son)