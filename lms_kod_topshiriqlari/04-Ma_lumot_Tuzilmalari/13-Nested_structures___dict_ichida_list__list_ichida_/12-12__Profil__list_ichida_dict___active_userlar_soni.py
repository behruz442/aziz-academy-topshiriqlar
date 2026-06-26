n = int(input().strip())
users = []
count = 0
for _ in range(n):
    username, active = input().split()
    users.append({'username': username, 'active': active == '1'})
    if active == '1':
        count += 1
        
print(count)
