def arttir(x):
    return x*1.2

personel = ["ali","veli","can","cemal","kemal"]
maas = [1000,2000,3000,4000,5000]
yeniMaas = list(map(arttir,maas))
sonuc = list(zip(personel,yeniMaas))

for i,k in sonuc:
    print("{} isimli personlein yeni maaşı: {}".format(i,k))

    