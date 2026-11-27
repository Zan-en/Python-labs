# пользователь создаёт список дел по категориям: учеба и т.д. развлечения, задается статус выполнено/не выполнено, после выполнения задачи
# пользователь сам меняет статус и в файл выводится название задачи время выполнения и статус

import time

history = []
def file(func):
    def wrapper(category, zadacha, status):
        zadachka = func(category, zadacha, status)
        history.append(zadachka)
        start_time = time.ctime()
        with open("zadachnik.txt", "a", encoding='utf-8') as f:
            f.write(f"Категория: {category}\n ")
            f.write(f"Задача категории {category}: {zadacha}\n ")
            f.write(f"Статус задачи {zadacha}: {status}, начало выполнения: {start_time}\n\n")
        return zadachka
    return wrapper

        
@file
def zadachki(category, zadacha, status):
    return category, zadacha, status





while True:

    choice = int(input("1.Добавить категорию и задачи для этой категории:\n " 
                       "2.Задать статус(Выполнено/не выполнено):\n " \
                       "3.Выйти\n" \
                       "Введите ваш выбор: "))

    match choice:
        case 1: 
            category = input("Введите категорию: ")
            zadacha = input("Введите задачи для категории: ")
            status = "Не выполнено"
            zadachki(category, zadacha, status)

        case 2:
            task = input(f"Выберите задачу для которой задать статус: ")
            status = input(f"Задайте статус для задачи - {task} (Выполнено/не выполнено): ").lower()
            if status == "выполнено":
                end_time = time.ctime()
                with open(f"zadachnik.txt", 'a', encoding='utf-8') as f:
                    f.write(f"Статус задачи {task}: {status}, конец выполнения: {end_time}\n\n ")
            else:
                continue                
        case 3:
            break

            


