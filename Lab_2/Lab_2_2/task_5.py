def cache(func):
    cache_list = {}
    def wrapper(*args, **kwargs):
        if (args in cache_list.keys()):
            print("in dec")
            return cache_list[args]
        else:
            result = func(*args, **kwargs)
            cache_list[args] = result
            return result
    return wrapper

@cache
def summmmmm(a, b):
    print("in func")
    return a + b

summmmmm(1, 2)
summmmmm(2, 3)
summmmmm(1, 2)
