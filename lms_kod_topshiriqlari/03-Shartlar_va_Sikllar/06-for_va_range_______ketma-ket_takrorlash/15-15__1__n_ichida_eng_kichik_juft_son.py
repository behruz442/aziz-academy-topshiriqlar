n = int(input())
print(next((i for i in range(2, n+1, 2)), "No"))