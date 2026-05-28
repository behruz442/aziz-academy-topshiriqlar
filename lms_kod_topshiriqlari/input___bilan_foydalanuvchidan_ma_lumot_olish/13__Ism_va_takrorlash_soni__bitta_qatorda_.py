s = input().strip()
name, count = s.split()
count = int(count)
result = (name + " ") * (count - 1) + name
print(result)