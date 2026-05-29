count = 0
while True:
    s = input()
    if s == "0":
        break
        
    a,b = map(int, s.split())
    
    x = input()
    
    count += 1
    
print(count)