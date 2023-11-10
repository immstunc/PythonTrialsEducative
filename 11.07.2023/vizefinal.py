vize = int(input("Vize notunuzu giriniz: "))
final =int(input("Final notunuzu giriniz: "))

ortalama= (vize*0.4) + (final*0.6)

if (ortalama>=50 and final>=50):
    print("Yıl sonu ortalamanız: ",ortalama ,"Dersten geçtiniz.")
else:
    print("Yıl sonu ortalamanız: ",ortalama , "Dersten kaldınız:(")