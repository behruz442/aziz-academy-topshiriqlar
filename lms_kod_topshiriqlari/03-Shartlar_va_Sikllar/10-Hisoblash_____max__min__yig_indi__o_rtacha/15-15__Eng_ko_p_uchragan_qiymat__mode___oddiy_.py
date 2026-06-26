input()
a = list(map(int,input().split()))
print(max(set(a), key=a.count))