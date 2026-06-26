n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append((int(price), name))
    
print(min(products)[1])