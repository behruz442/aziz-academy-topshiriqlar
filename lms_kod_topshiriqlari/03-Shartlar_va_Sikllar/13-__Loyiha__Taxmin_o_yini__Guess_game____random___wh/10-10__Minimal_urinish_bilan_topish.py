s, n = 1, 0
while True:
    n += 1
    if int(input()) == s:
        print(f"Correct\n{n}")
        break
    print("Try again")