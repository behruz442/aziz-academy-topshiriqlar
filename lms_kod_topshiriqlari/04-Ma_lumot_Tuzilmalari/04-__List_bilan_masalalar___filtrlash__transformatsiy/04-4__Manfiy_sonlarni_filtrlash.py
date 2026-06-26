n = int(input())
lst = list(map(int, input().split()))
manfiylar = [x for x in lst if x < 0]
print(manfiylar)