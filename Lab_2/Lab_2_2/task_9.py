def type_check(type1, type2):
    def dec(func):
        def wrapper(*args, **kwargs):
            if not isinstance(args[0], type1) or not isinstance(args[1], type2):
                raise TypeError("Неверные типы!")
            return func(*args, **kwargs)
        return wrapper
    return dec

@type_check(int, int)
def summmmmm(a, b):
    return a + b

summmmmm(1, 2)
summmmmm("1", 2)