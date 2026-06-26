n = int(input())
words = input().split()
result = []
vowels = set('aeiou')
for i in words:
    if len(i) >= n:
        result.append(i)
        
print(result)