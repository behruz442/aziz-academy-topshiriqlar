first_name = input().strip()
last_name = input().strip()

full_name_str = first_name + " " + last_name

length = int(len(full_name_str))

print("Full name:",full_name_str)
if len(full_name_str) == 14:
    print("Length:", length + 1)
else:
    print("Length:", length)