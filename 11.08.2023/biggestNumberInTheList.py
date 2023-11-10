liste = []
adet = int(input("Kaç tane sayı gireceksiniz? : "))

print("{} adet sayı gireceksiniz".format(adet))

for n in range(adet):
    sayi = int(input("{}. sayıyı girin: ".format(n+1)))
    liste.append(sayi)

enKucuk = liste[0]
enBuyuk = liste[0]

for n in liste:
    if enKucuk > n:
        enKucuk = n
    
    if enBuyuk < n:
        enBuyuk = n

'''#bu yönteme alternatif algoritmasız yöntem=>>>
enKucuk = min(liste)
enBuyuk = max(liste)'''

print("Listedeki en büyük sayı : {}\nListedeki en küçük sayı : {}"
      .format(enBuyuk,enKucuk))



