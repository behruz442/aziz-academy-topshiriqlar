s = -4
while True:
    g = int(input())
    if g == s:
        print("Correct")
        break
    print("High" if g > s else "Low")