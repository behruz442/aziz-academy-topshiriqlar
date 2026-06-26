n = int(input())
c = 0
i = 1
while i <= n:
    if i % 2 == 0:
        c += 1
        if  c == 3:
            print(i)
            break
    i += 1
else:
    print("No")
