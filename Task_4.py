stroka = input("Введите строку: ")
reversestroka= stroka[::-1]
if reversestroka == stroka:
    print(f" {stroka}  - это палиндром, т.к. {stroka}={reversestroka}")
else:
    print(f" {stroka} - это не палиндром, т.к. {stroka}≠{reversestroka}")