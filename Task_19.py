def cache(func):
    dictionary = {}
    def wrapper(*args):
        if args not in dictionary:
            dictionary[args] = func(*args)
        return dictionary[args]
    return wrapper


@cache

def umnozh(i,j):
    return i*j

print(f"Первый вывод, где записали в словарь - {umnozh(3,4)}")
print(f"Второй вывод, где возвращаем значение просто сразу - {umnozh(3,4)}")    