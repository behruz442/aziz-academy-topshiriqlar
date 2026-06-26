n = int(input())
totals = {}
for _ in range(n):
    data = input().split()
    cat, price, qty = data[0], int(data[2]), int(data[3])
    totals[cat] = totals.get(cat, 0) + (price * qty)
    
for cat in sorted(totals):
    print(f"{cat} {totals[cat]}")