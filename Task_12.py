vvod = input("Введите ваш текст: ").lower()
slova = vvod.split()


for i in range(2):
    kolvo_slov = len(slova)
print(f"Кол-во слов: {kolvo_slov}")
razn_slova = {}
for slovo in slova:
    if slovo in razn_slova:
        razn_slova[slovo] += 1
    else:
        razn_slova[slovo] = 1
for slovo in razn_slova:
    print(f"Слово {slovo} найдено в тексте - {razn_slova[slovo]} раз")







