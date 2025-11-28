import time
def timing(func):
    def wrapper(*args, **kwargs):
        time_before = time.perf_counter()
        result = func(*args, **kwargs)
        time_after = time.perf_counter()
        exe_time = (time_after - time_before)*1000
        print(f"Время выполнения функции '{func.__name__}': {exe_time:.2f} мс")
        return result
    return wrapper

@timing
def f(name):
    a = input("Press F to pay respect: ").lower()
    if (a == "f"):
        print(f"{name}, you paid respect!")
    else:
        print("FAQ")

f("Алексей")

@timing
def summmmmm(a, b):
    return a + b

summmmmm(13154657657658753454353, 232766576575676547665)
summmmmm(1, 2)

@timing
def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact
    
print(factorial(1211))


