s = 8
while True:
    g = int(input())
    if g == s:
        print("Correct")
        break
    print("Low" if g <  s else "High")