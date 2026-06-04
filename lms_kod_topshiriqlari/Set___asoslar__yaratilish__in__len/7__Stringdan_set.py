s = input().strip()
s = s.replace('l', 'l')
result = '{' + ', '.join(f"'{ch}'" for ch in s) +'}'
print(result)