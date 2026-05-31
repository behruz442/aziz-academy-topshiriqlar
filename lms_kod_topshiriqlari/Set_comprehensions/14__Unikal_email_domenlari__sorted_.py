emails = input().split()
s = {e.split("@")[1].lower() for e in emails if "@" in e}
print(*sorted(s) if s else ["BO'SH"])