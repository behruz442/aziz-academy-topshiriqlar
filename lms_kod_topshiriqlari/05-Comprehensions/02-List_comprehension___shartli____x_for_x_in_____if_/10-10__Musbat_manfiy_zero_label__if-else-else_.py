nums = list(map(int, input().split()))

labels = ['pos' if x > 0 else 'neg' if x < 0 else 'zero' for x in nums]
print(' '.join(labels))