# Bank Transaksiyalarini Hisoblash
# Kurs: IT Dasturlash
# Mavzu: 1-mavzu: Python va dasturlashga kirish
# Ball: 100
# Aziz Academy — AI Topshiriq

jami = 0
while True:
    kiritish = input()
    if kiritish == "stop":
        break
        
    if kiritish.isdigit():
        qiymat = int(kiritish)
    else:
        if kiritish == "kirim":
            jami += qiymat
        elif kiritish == "chiqim":
            jami -= qiymat
            
print(f"Jami hisob: {jami}")