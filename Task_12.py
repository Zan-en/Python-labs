vvod = input("Введите ваш текст: ").lower()
slova = vvod.split()


for i in range(2):
    kolvo_slov = len(slova)
    print(f"\033[1mКол-во слов: {kolvo_slov}\033[0m")
    razn_slova = {}
    for slovo in slova:
        if slovo in razn_slova:
            razn_slova[slovo] += 1
        else:
            razn_slova[slovo] = 1
    for slovo in razn_slova:
        print(f"Слово {slovo} найдено в тексте - {razn_slova[slovo]} раз")
    max_value = max(razn_slova.values())
    bolshe_razn_slovo = []


    for j in razn_slova:
        if razn_slova[j] == max_value:
            bolshe_razn_slovo.append(j)
    resultatraznix = ""

    for bslv in bolshe_razn_slovo:
        resultatraznix += bslv + " "
        print(f"Слово {resultatraznix}имеет наибольшее кол-во повторений")
        dlin_slov =[]

    for slovo in razn_slova:
        dlin_slov.append(len(slovo))
        max_dlina = max(dlin_slov)
        min_dlina = min(dlin_slov)
        naibolsh_slovo = []
        naimensh_slovo = []
    for slovo in razn_slova:
        if len(slovo) == max_dlina:
            naibolsh_slovo.append(slovo)
        if len(slovo) == min_dlina:
            naimensh_slovo.append(slovo)
        naibolsh = ""
        for bslv in naibolsh_slovo:
            naibolsh += bslv + " "
        naimensh = ""
        for bslv in naimensh_slovo:
            naimensh += bslv + " "
        proshliproverku = []
        for slovo in slova:
            if len(slovo) >= 3:
                proshliproverku.append(slovo)
    slova = proshliproverku
    print(f"Самое длинное: {naibolsh},   Самое короткое: {naimensh};")