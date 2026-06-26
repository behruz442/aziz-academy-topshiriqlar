lst = [1, 2, 3]
n = int(input())

if n in lst:
    lst.remove(n)
    print("Removed")
else:
    print("Not found")
  
print(lst)