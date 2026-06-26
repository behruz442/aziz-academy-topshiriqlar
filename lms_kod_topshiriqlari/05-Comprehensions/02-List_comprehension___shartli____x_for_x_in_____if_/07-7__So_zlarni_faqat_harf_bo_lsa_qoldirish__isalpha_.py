tokens = input().split()

alphas = [t for t in tokens if t.isalpha()]
if not alphas:
    print("BO'SH")
else:
    print(' '.join(alphas))