day = int(input("Введите день вашего рождения: "))
month = int(input("Введите месяц вашего рождения: "))
year = int(input("Введите год вашего рождения: "))

isdcorrect = True

if not (1 <= month <= 12):
    isdcorrect = False

if isdcorrect:
    if day < 1:
        isdcorrect = False
    else:
       
        if month in (1, 3, 5, 7, 8, 10, 12):
            maximalday = 31
        elif month in (4, 6, 9, 11):
            maximalday = 30
        else: 
         
            isdvisok = (year % 4 == 0)
            maximalday = 29 if isdvisok else 28
        
        if day > maximalday:
            isdcorrect = False

if not isdcorrect:
    print("Неккоректно введена дата")
    exit()
    
match(month, day):
 case(4, d) if d < 20:
  print("Овен")
 case(4,d) if d >=20:
  print("Телец")
 case(5,d) if d <=20:
  print("Телец")
 case(5,d) if d > 20:
  print("Близнецы")
 case(6, d) if d <=20:
  print("Близнецы")
 case(6, d) if d >20:
  print("Рак")
 case(7, d) if d<=22:
   print("Рак")
 case(7, d) if d >22:
   print("Лев")
 case(8, d) if d <=22:
  print("Лев")
 case(8, d) if d >22:
  print("Дева")
 case(9, d) if d <=22:
  print("Дева")
 case(9,d) if d >22:
  print("Весы")
 case(10, d) if d <=22:
  print("Весы")
 case(10, d) if d >22:
  print("Скорпион")
 case(11, d) if d<=21:
   print("Скорпион")
 case(11, d) if d >22:
  print("Стрелец")
 case(12, d) if d<=21:
  print("Стрелец")
 case(12, d) if d>21:
  print("Козерог")
 case(1,d) if d<=20:
  print("Козерог")
 case(1,d) if d >20:
  print("Водолей")
 case(2,d) if d <=20:
  print("Водолей")
 case(2,d) if d>20:
  print("Рыбы")
 case(3,d) if d <=20:
  print("Рыбы")
 case(3,d) if d >20:
   print("Овен")