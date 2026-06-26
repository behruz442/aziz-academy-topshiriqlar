n = int(input())
a = list(map(int,input().split()))
for i in range(n):
    if a[i]%2<i:
        print(i)
        break
    elif a[-1] == 7:
        print(-1)
        break
