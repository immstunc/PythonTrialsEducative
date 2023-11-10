s1 = int(input("birinci sayıyı giriniz: "))
s2 = int(input("ikinci sayıyı giriniz: "))
s3 = int(input("üçüncü sayıyı giriniz: "))

buyuk = s1

if s2 > buyuk:
    buyuk = s2

if s3 > buyuk:
    buyuk = s3

print("girilen en büyük sayı: ",buyuk)