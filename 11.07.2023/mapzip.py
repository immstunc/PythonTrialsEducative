def arttir(x):
    return x*1.2

personel = ["Selva", "Hamza", "Merve", "Ali", "Veli"]
maas= [1000,2000,2500,3000,5000]

yeniMaas = list(map(arttir,maas))
sonuc= list(zip(personel,yeniMaas))
print(sonuc)