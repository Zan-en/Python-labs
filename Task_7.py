freeminutes = 60
freemegabytes = 1000
freesms=30
tariff_price =24.99

minutes = int(input("Напишите кол-во потраченных за месяц минут: "))
megabytes = int(input("Напишите кол-во потраченных за месяц мегабайт: "))
sms = int(input("Напишите кол-во потраченных за месяц сообщений: "))

if megabytes <= freemegabytes:
    plat_megabytes =0
else:
    plat_megabytes = (megabytes - freemegabytes)*0.79

if minutes <= freeminutes:
    plat_minutes =0
else:
    plat_minutes = (minutes - freeminutes)*0.89

if sms <= freesms:
    plat_sms=0
else:
    plat_sms = (sms - freesms)*0.59

polnaya_tariff_price = tariff_price + plat_minutes + plat_megabytes + plat_sms
nalog= polnaya_tariff_price * 0.02
print(f"Изначальный тариф: {tariff_price} рублей")

if plat_sms !=0:
    print(f"Плата за дополнительные смс : {plat_sms:.2f} рублей")
if plat_megabytes !=0:
     print(f"Плата за дополнительные мегабайты : {plat_megabytes:.2f} рублей")
if plat_minutes !=0:
     print(f"Плата за дополнительные минуты : {plat_minutes:.2f} рублей")
print(f"Налог: {nalog:.2f} рублей")
print(f"Общая стоимость тарифа: {polnaya_tariff_price+nalog:.2f} рублей")