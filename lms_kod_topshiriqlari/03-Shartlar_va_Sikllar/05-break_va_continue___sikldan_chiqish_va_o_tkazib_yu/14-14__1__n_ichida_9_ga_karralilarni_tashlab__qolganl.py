n = int(input())
s = 0
i = 1
while i <= n:
    if i % 9:
        s += i
    i += 1
print(s)