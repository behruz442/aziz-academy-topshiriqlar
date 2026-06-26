s = c = 0
n = int(input())
while n:
    s += n
    c += 1
    n = int(input())
print(s/c if c else 0)