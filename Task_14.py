nabor_1 = input("Введите первый список чисел через пробел: ").split(" ")
nabor_2 = input("Введите второй список чисел через пробел: ").split(" ")

chisla_1 = []
chisla_2 = []

for i in nabor_1:
    chisla_1.append(int(i))
for i in nabor_2:
    chisla_2.append(int(i))


chisla_11 = set(chisla_1)
chisla_22 = set(chisla_2)
print(f"Первый набор чисел: {chisla_1}")
print(f"Второй набор чисел: {chisla_2}")

odinakovye = chisla_11 & chisla_22
otsutvo2 = chisla_11 - chisla_22
otsutv1 = chisla_22 - chisla_11
obyed1and2 = chisla_11 | chisla_22
chislaizoboih = obyed1and2 - odinakovye


print(f"1.Одновременно в двух наборах: {odinakovye}")
print(f"2.Отсутствуют в первом: {otsutv1}")
print(f"2.Отсутствуют во втором: {otsutvo2}")
print(f"3.Числа из обоих без первого пункта: {chislaizoboih}")