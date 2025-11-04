def type_check(type1, type2):
    def dec(func):
        def wrapper(*args, **kwargs):
            if len(args) >= 1 and not isinstance(args[0], type1):
                raise TypeError(f"Неверные типы!")
            if len(args) >= 2 and not isinstance(args[1], type2):
                raise TypeError(f"Неверные типы!")
            return func(*args, **kwargs)
        return wrapper
    return dec

@type_check(int, int)
def summmmmm(a, b):
    return a + b

summmmmm(1, 2)
summmmmm("1", 2)