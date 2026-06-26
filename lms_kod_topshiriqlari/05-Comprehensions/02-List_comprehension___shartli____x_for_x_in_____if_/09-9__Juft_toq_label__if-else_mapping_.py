nums = list(map(int, input().split()))

labels = ['even' if x % 2 == 0 else 'odd' for x in nums]
print(' '.join(labels))