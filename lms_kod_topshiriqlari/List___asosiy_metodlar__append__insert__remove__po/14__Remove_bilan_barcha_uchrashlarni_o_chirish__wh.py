n = int(input())

lst = list(map(int, input().split()))
lst2 = []
target = int(input())

for i in lst:
    if i == target:
        continue
    else:
        lst2.append(i)
print(lst2)