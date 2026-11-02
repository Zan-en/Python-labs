import time


def log_calls(file):
    def decorator(func):
        def wrapper(*args):
            with open(file, 'a') as f:
                f.write(
                    f"{time.strftime("%Y-%m-%d %H:%M:%S")}\t" #В этой строчке сделал просто более удобный и общепринятый вывод даты и времени в файл
                    f"{func.__name__}\t"
                    f"{", ".join(map(str, args))}\t\n"
                )
            return func(*args)
        return wrapper
    return decorator

@log_calls("text.txt")
def funcia(slovo):
    print(slovo)


funcia("Ananas")
funcia("Medvedi")
