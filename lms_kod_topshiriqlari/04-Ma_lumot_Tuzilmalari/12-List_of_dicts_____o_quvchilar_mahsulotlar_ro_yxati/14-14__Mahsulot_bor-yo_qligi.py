n = int(input())
names = {input().split()[0] for _ in range(n)}
x = input().strip()

print("YES" if x in names else "NO")