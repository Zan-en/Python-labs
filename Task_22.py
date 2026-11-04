def type_check(*types):
    def decorator(funcia):
        def wrapper(*args):
            for arg in range(len(args)):
                if not isinstance(args[arg], types[arg]):
                    raise TypeError(f"Аргумент {arg} не является соответствующим типом {types[arg].__name__}")

            return funcia(*args)
        return wrapper
    return decorator

@type_check(int, float)
def delenie(a,b):
    return a/b
print(f"Результат выполнения функции деления: {delenie(25, 1.25)}")