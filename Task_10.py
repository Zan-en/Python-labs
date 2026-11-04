summ=float(input("На сколько денег вы закупились? "))
age=int(input("Сколько вам лет? "))
birthday=input("У вас сегодня день рождения?(да/нет) ").replace(" ", "")
is_VIP = input("У вас есть карточка ВИП-клиента?(да/нет) ").replace(" ", "")
max_discount= 0.25


if is_VIP == "да".lower():
    VIPdiscount = True
elif is_VIP == "нет".lower():
    VIPdiscount= False

if birthday == "да".lower():
    HBdiscount = True
elif birthday == "нет".lower():
    HBdiscount= False

if summ > 1000:
    summ_discount = 0.1
elif summ < 1000:
    summ_discount = 0

if age >= 63 :
    age_discount = 0.05
elif age <= 63:
    age_discount = 0

if HBdiscount == True:
    HBdiscount = 0.05
else:
    HBdiscount = 0

if VIPdiscount == True:
    VIPdiscount = 0.15
else:
    VIPdiscount = 0


all_discount = VIPdiscount + summ_discount + age_discount + HBdiscount 

if all_discount > max_discount:
    all_discount = max_discount
else:
    max_discount = all_discount

itog_price =summ - (summ * max_discount)
discount_price = summ * max_discount

print(f"Цена с учетом скидки: {itog_price:.2f}")
print(f"Сумма скидки: {discount_price:.2f}")
