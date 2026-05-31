n = int(input().strip())
items = []
for _ in range(n):
    name, price, qty = input().split()
    items.append({'name': name, 'price': int(price), 'qty': int(qty)})
    
if items:
    top_item = max(items, key=lambda x: x['price'] * x['qty'])
    
    print(top_item['name'])