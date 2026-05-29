a,b = map(int,input().split())
choice = int(input())

if a<0 or b < 0:
    print("Invalid")
elif choice == 1:
    print(a+b)
else:
    print("Invalid")