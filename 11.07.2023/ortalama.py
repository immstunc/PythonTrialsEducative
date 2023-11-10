nums = []

while True:
    num=int(input("Bir sayı girin:"))
    if num==0:
        break
    nums.append(num)

total=sum(nums)
count=len(nums)

print("Sayıların ortalaması:", total/count)
