words = input().split()

long_words = [w for w in words if len(w) >= 5]
if not long_words:
    print("BO'SH")
else:
    print(' '.join(long_words))