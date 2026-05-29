l = []
while True:
    c = input().split()
    if c[0] == "append":
        l.append(int(c[1]))
    elif c[0] == "insert":
        l.insert(int(c[1]), int(c[2]))
    elif c[0] == "remove" and int(c[1]) in l:
        l.remove(int(c[1]))
    elif c[0] == "pop":
        l.pop(int(c[1]))
    elif c[0] == "stop":
        break
print(l)