import math

r = float(input("Yarıçapı giriniz: "))
area = round(math.pi * r * r,2)
perimeter = round(math.pi * 2 * r,2)

print("Çemberin alanı: ",area)
print("Çemberin çevresi: ",perimeter)