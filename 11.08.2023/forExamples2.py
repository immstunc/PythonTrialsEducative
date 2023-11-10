#girilen iki sayı arasındaki 5'e bölünen sayıları ekrana yazdır

'''sayi1 = int(input("1.sayıyı giriniz : "))
sayi2 = int(input("2.sayıyı giriniz : "))

for i in range(sayi1,sayi2+1): #sayi2kapsansın diye +1
    if i%5==0:
        print(i)'''

#kullanıcıdan alınan iki sayı arasındaki sayıların toplamı

'''print("Küçükten büyüüğe herhangi iki sayıgiriniz")
n1 = int(input("1.sayıyı giriniz : "))
n2 = int(input("2.sayıyı giriniz : "))

toplam = 0

for t in range(n1,n2+1):
    toplam+=t

print("Sayıların toplamı : ",toplam)'''

#kullanıcıdan alınan iki sayı arasındaki çift sayıların toplamı

'''print("Küçükten büyüğe herhangi iki sayıgiriniz")
n1 = int(input("1.sayıyı giriniz : "))
n2 = int(input("2.sayıyı giriniz : "))

toplam = 0

for t in range(n1,n2+1):
    if t%2==0:
      toplam+=t

print("Sayıların toplamı : ",toplam)'''

#girilen sayını çarpım tablosunu yazdır

'''sayi=int(input
         ("çarpım tablosuna hoşgeldiniz\nÇarpım tablosunu görmek istediğiniz sayıyı giriniz : "))


for i in range(1,11):
    print("{} x {} = {}".format(sayi,i,sayi*i))
'''

#girilen 2 sayı arasındaki 3'e bölünenler - 5'e bölünenleri ekrana yazdır
print("Küçükten büyüğe herhangi iki sayıgiriniz")
n1 = int(input("1.sayıyı giriniz : "))
n2 = int(input("2.sayıyı giriniz : "))

fark = 0

for (t,k) in range(n1,n2+1):
    if t%3==0 and k%5==0:
      fark = t - k

print("Girilen aralıkta 3'e bölünen sayılar ile 5'e bölünen sayıların farkı  : {} - {} = ".format(t,k),fark)
