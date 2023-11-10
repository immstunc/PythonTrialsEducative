toplam = 0
while True:
    sayi = int(input("Bir sayı giriniz:"))
    if sayi == 0:
        break
    toplam+=sayi

print("Sayıların toplamı = " ,toplam)