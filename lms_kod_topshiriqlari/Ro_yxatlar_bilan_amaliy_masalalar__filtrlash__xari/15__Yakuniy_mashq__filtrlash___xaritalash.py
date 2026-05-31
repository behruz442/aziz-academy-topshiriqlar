n = int(input())

sonlar = list(map(int, input().split()))

natija = [ x * 2 for x in sonlar if x > 0]

print(natija)