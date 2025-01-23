import random
karakterler="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int(input("şifre kaç haneli olsun?"))

sifre = ""

for i in range(uzunluk):
    sifre += random.choice(karakterler)

print(sifre)
