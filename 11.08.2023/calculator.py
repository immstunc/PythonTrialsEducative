def Topla(a,b):
    return a+b

def Cikar(a,b):
    return a-b

def Carp(a,b):
    return a*b

def Bol(a,b):
    return a/b


print("Yapılacak işlemi seçin: \n1.Toplama\n2.Çıkarma\n3.Çarpma\n4.Bölme")

secim = input("Bir seçim girin: ") 
sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

if secim == "1":
    print("Toplama Sonucu = ",Topla(sayi1,sayi2))
elif secim == "2":
    print("Çıkarma Sonucu = ",Cikar(sayi1,sayi2))
elif secim == "3":
    print("Çarpma Sonucu = ",Carp(sayi1,sayi2))
elif secim == "4":
    print("Bölme Sonucu = ",Bol(sayi1,sayi2))
else: 
    print("Hatalı seçim yaptınız.")
