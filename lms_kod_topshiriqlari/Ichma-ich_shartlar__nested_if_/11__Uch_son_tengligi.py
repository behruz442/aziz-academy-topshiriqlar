a, b, c = map(int, input().split())


if b == c and a == c and a == b:
    print("All equal")
elif a == c or b == c or a == b:
    print("Partially equal")
else:
    print("All different")
        
        