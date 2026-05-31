n = int(input())
print(f"{'Name':<10} | Score")
print("-"*10+"+"+"-"*5)
for _ in range(n):
    a, b = input().split()
    print(f"{a:<10} | {int(b):>5}")