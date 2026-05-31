text = input()

digits = [ch for ch in text if ch.isdigit()]

if not digits:
    print("BO'SH")
else:
    print(''.join(digits))