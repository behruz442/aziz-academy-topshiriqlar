n = int(input().strip())
users = []
all_tags = set()
for _ in range(n):
    parts = input().split()
    username = parts[0]
    k = int(parts[1])
    tags = parts[2:2+k]
    users.append({'username': username, 'tags': tags})
    all_tags.update(tags)
    
print(len(all_tags))