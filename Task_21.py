import time 
def timing(funcia):
    def wrapper(*args):
        nachalo = time.perf_counter()
        resultat = funcia(*args)
        konec = time.perf_counter()
        print(f"Время выполнения: {(konec-nachalo)*1000:.3f} миллисекунд")
        return resultat
    return wrapper

@timing
def zamer():
    a = float(input("Напишите первое число для умножения: "))
    b = float(input("Напишите второе число для умножения: "))
    print(f"Вывод: {a*b}")

zamer()
