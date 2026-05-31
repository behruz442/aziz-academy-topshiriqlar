n = int(input().strip())
users = []
max_tags = -1
max_user = ""
for _ in range(n):
    parts = input().split()
    username = parts[0]
    k = int(parts[1])
    tags = parts[2:2+k]
    users.append({'username': username, 'tags': tags})
    
    if k > max_tags:
        max_tags = k
        max_user = username
        
print(max_user)