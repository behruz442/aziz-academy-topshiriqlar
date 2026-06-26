n = int(input())

sonlar = list(map(int, input().split()))

orta = n - (n // 2)

natija = sonlar[orta:]

print(natija)