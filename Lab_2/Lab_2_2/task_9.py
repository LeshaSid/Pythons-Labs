def type_check(*args1):
    def dec(func):
        def wrapper(*args2, **kwargs):
            for i in range(len(args2)):
                if not isinstance(args2[i], args1[i]):
                    raise TypeError("Неверные типы!")
            return func(*args2, **kwargs)
        return wrapper
    return dec

@type_check(int, int)
def summmmmm(a, b):
    return a + b

@type_check(int, int, int, int)
def summmmmm2(a, b, c, d):
    return a + b + c + d


print(summmmmm(1, 2))
summmmmm("1", 2)

print(summmmmm2(1, 2, 3, 4))
summmmmm2(1, "2", 3, 4)