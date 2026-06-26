n = int(input())
total_price = 0
for i in range(n):
    line = input().split()
    price = int(line[1])
    total_price += price
    
print(total_price)