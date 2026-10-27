import random

ugad_chislo = random.randint(1, 100)



while True:
    chislo = int(input("Попробуйте угадать число, для этого введите догадку: "))
    if chislo > ugad_chislo:
        print("Загаданное число меньше. Попробуйте ещё раз ")
    elif chislo < ugad_chislo: 
        print("Загаданное число больше. Попробуйте ещё раз ")
    else:
        print(f"Вы выиграли, поздравляю!")
        break

