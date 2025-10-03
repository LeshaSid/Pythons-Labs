import time
def timing(func):
    def wrapper(*args, **kwargs):
        time_before = time.time()
        result = func(*args, **kwargs)
        time_after = time.time()
        print(f"Время выполнения функции: {(time_after - time_before)*1000} мс")
        return result
    return wrapper

@timing
def f(name):
    a = input("Press F to pay respect: ")
    a.lower()
    if (a == "f"):
        print(f"{name}, you paid respect!")
    else:
        print("FAQ")

f("Алексей")

@timing
def summmmmm(a, b):
    return a + b

summmmmm(131543, 2326547665)

