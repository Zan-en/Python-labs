vvod = input("Введите числа через пробел: ").split(" ")
chisla = []


for chislo in vvod:
    if float(chislo).is_integer():
        chisla.append(int(chislo))
    else:
        chisla.append(float(chislo))

    unique = []
    povtor= []
    chet = []
    nechet = []
    menshenull = []
    plav_tochka = []
    summa_5 = 0

    for i in chisla:
        count = 0
        for j in chisla:
            if i == j:
                count += 1
        if count == 1:
            unique.append(i)
        if count > 1 and i not in povtor:
            povtor.append(i)

    for i in chisla:
        if i == int(i):
            if i % 2 == 0:
                chet.append(i)
            else:
                nechet.append(i)

    for i in chisla:
        if i < 0:
            menshenull.append(i)

    for i in chisla:
        if i != int(i):
            plav_tochka.append(i)

    for i in chisla:
        if i==int(i) and int(i) % 5 == 0:
            summa_5 += i

    naib_chislo = chisla[0]
    for i in chisla:
        if i > naib_chislo:
            naib_chislo = i
    naim_chislo = chisla[0]
    for i in chisla:
        if i < naim_chislo:
            naim_chislo = i

print(f"Уникальные числа: {unique}")
print(f"Повторяющиеся: {povtor}")
print(f"Четные: {chet};   Не четные: {nechet}")
print(f"С плавающей точкой: {plav_tochka}")
print(f"Сумма чисел кратных 5: {summa_5}")
print(f"Наибольшее число: {naib_chislo};   Наименьшее число: {naim_chislo}")
