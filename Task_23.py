zarabotnaya = float(input("Введите свою зп: "))
zhile = float(input("Введите стоимость аренды жилья: "))
ezha = float(input("Введите сколько денег уходит на еду: "))
transport = float(input("Введите сколько уходит на транспорт: "))
razvlecheniya = float(input("Сколько уходит на развлечения? "))
abonement = float(input("Введите стоимость абонемента в зал: "))
tarif = float(input("Введите стоимость тарифа связи: "))
kv = float(input("Квартира которую хотите купить сколько стоит? "))

kray_zhile = zarabotnaya * .30
kray_ezha = zarabotnaya * .2
kray_transport = zarabotnaya * 0.1
kray_razvlech = zarabotnaya * .1
kray_abonement = zarabotnaya * .03
kray_tarif = zarabotnaya * .02
min_podushka = zarabotnaya * .25

skolko = zhile + ezha + transport + razvlecheniya + abonement + tarif
podushka = zarabotnaya - skolko
print(f"Уходит денег в месяц: {skolko}")
print(f"Откладывается на квартиру: {podushka}")

if zarabotnaya < skolko:
    print(f"Надо работать больше и кормить детей, а на этот месяц займи ещё вот столько: {skolko - zarabotnaya}")
if zhile > kray_zhile:
    print(f"Бро, либо работай больше либо готовься съезжать, с твоим доходом максимум за аренду вот {kray_zhile}")
if ezha > kray_ezha:
    print(f"Пора худеть, а кошельку толстеть, столько максимум надо тратить на еду - {kray_ezha}")
if transport > kray_transport:
    print(f"Не, давай без такси в этом месяце, а то так не проживешь, вот твой максимум - {kray_transport}")
if razvlecheniya > kray_razvlech:
    print(f"Ты много отдыхал, пора поработать, максимум на развлечения - {kray_razvlech}")
if abonement > kray_abonement:
    print(f"Найди зал подешевле ты и так масса, например, за вот такую стоимость - {kray_abonement}")
if tarif > kray_tarif:
    print(f"Меняй оператора связи, желательно за такую стоимость - {kray_tarif}")
if podushka >= min_podushka:
    print(f"А ты хорош, отложил на квартиру не хило")
elif podushka < min_podushka >= 0:
    print(f"Бро, на квартиру надо копить, откладывай минимум столько - {min_podushka}")
else:
    print(f"Я конечно не эксперт, но лучше отложи на квартиру, она и так стоит {kv}, а ты тратишь куда-то")
