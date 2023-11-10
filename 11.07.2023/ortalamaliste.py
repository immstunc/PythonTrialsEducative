liste = [10,20,30,40,50,60,100,80]
adet = len(liste)
toplam = 0

for sayi in liste:
    toplam+=sayi

ortalama=toplam/adet
print("Sayıların ortalamsı: ",ortalama)