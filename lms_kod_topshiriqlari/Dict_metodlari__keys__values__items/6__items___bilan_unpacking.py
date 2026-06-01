n = int(input())
data = []
for _ in range(n):
    line = input().split()
    data.append(line)
for item in data:
    print(item[0], item[1])