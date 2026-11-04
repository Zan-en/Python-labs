age = int(input("Введите ваш возраст: "))
zp = float(input("Введите ваш ежемесячный доход: "))
credit_amount = float(input("На какую сумму вы хотите взять кредит? "))
credit_length = int(input("За какой период времени вы сможете выплатить кредит?(в месяцах) "))
credit_history = input("Ваша кредитная история?(отличная/ хорошая / удовлетворительная / плохая)? ").replace(" ", "")
poruch = input("Есть ли поручители?(да / нет) ").replace(" ", "")
deposit= input("Есть ли залог?(да / нет) ").replace(" ", "")

month_viplata = credit_amount / credit_length 
viplata = (month_viplata / zp) * 100

if credit_history == "отличная":
    risk = "минимальный"
elif credit_history == "хорошая":
    risk = "средний"
elif credit_history == "удовлетворительная":
    risk = "высокий"
else:
    risk = "МАКСИМАЛЬНЫЙ"

if viplata > zp*0.4 or age < 21 or age > 63:
    risk = "МАКСИМАЛЬНЫЙ"
if poruch == "да" and deposit =="да":
    if risk == "МАКСИМАЛЬНЫЙ":
        risk = "высокий"
    elif risk == "высокий":
        risk = "средний"

if risk == "минимальный":
        stavka = 10
        vyvod = "Одобрят 100%"
elif risk == "средний":
        stavka = 17.5
        vyvod = "Одобрят с вероятностью 70%"
elif risk == "высокий":
        stavka = 23
        vyvod = "Одобрят с вероятностью 30%"
else:
        stavka = 0
        vyvod = "Отказано в кредите"


print(f"Ежемесячная выплата по кредиту: {month_viplata:.2f}")
print(f"Доход банка в процентах к сумме кредита : {viplata:.2f}%")
print(f"Риск не одобрения: {risk}")

if stavka > 0:
        print(f"Кредит под {stavka:.1f}% годовых")

print(f"Вывод одобрения по кредиту: {vyvod}")