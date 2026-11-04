vvod= input("Введите единицы измерения (масса или время или площадь): ")

izmereniya ={
    "масса" : "мг/г/кг/т",
    "время" : "с/мин/час",
    "площадь" : "м^2 / га / км^2"

}


begin_izmerenie = input(f"Введите начальную единицу измерения: {izmereniya[vvod]}: ")
end_izmerenie = input(f"Введите конечную единицу измерения: {izmereniya[vvod]}: ")
znach_vvod = float(input("Введите значение чтобы перевести из одной в другую: "))


izmereniya_converter = {
    "мг" : 1000000,
    "г" : 1000,
    "кг" : 1,
    "т" : 0.001,
    "с" : 3600,
    "мин" : 60,
    "час" : 1,
    "м^2" : 1000000,
    "га" : 100,
    "км^2" : 1
}


result = znach_vvod * izmereniya_converter[end_izmerenie] / izmereniya_converter[begin_izmerenie]
print(f"Переведенное: {vvod} {znach_vvod} {begin_izmerenie} = {result:.2f} {end_izmerenie}")