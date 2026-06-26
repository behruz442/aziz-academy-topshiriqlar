s, n = 20, 0
while True:
    g, n = int(input()), n + 1
    if g == s:
        print(f"Correct\n{n}")
        break
    print("Invalid" if g > s else "Low")