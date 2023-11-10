import datetime

birthYear = int(input("Doğum yılınızı griniz(YYYY): "))
 
todayDate = datetime.datetime.now()
todayYear = todayDate.year

age = todayYear - birthYear

print("Merhaba \nDoğum yılınız: {} \nYaşınız: {}"
      .format(birthYear,age))