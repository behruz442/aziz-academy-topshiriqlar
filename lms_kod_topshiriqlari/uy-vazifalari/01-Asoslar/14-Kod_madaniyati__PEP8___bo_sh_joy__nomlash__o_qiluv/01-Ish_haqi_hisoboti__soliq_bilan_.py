ish = int(input())
kunlik = int(input())
soliq_foizi = int(input())

yalpi = ish * kunlik
soliq_summasi = yalpi * soliq_foizi // 100
qolgan_summa = yalpi - soliq_summasi

print(yalpi)
print(soliq_summasi)
print(qolgan_summa)