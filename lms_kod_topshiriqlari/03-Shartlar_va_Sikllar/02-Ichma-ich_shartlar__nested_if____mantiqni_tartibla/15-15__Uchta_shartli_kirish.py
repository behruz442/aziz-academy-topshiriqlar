ism, holat = input().split()
holat = int(holat)

if ism == "admin":
    if holat == 1:
        print("Admin active")
    else:
        print("Admin inactive")
else:
    if holat == 1:
        print("User active")
    else:
        print("User")