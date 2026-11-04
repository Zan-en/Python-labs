
summ = int(input("Введите сумму в рублях(без копеек): "))
skolko100 = summ // 100
ostatokposle100 = summ % 100
skolko50 = ostatokposle100 // 50
ostatokposle50 = ostatokposle100 % 50
skolko10 = ostatokposle50 // 10
ostatokposle10 = ostatokposle50 % 10
skolko5 = ostatokposle10 // 5 
ostatokposle5 = ostatokposle10 % 5
skolko2 = ostatokposle5 // 2
ostatokposle2 = ostatokposle5 % 2
skolko1 = ostatokposle2 


print(f"Купюр по 100: {skolko100}; Купюр по 50: {skolko50}; Купюр по 10: {skolko10}; Купюр по 5: {skolko5}, Монет по 2: {skolko2}; Монет по рублю: {skolko1}")

