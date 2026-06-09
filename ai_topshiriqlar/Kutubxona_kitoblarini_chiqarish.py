# Kutubxona kitoblarini chiqarish
# Kurs: IT Dasturlash
# Mavzu: 2-mavzu: Birinchi dastur, print() va kommentlar
# Ball: 100
# Aziz Academy — AI Topshiriq

n = int(input())
for i in range(n):
    malumot = input().split()
    kitob = malumot[0]
    muallif = malumot[1]
    print(f"{kitob}, {muallif}")