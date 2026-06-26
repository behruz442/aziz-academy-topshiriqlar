words = input().split()

result = [w.lower() for w in words if w.lower().startswith('a')]

if not result:
    print("BO'SH")
else:
    print(' '.join(result))