from datetime import datetime
def log_calls(filename):
    def dec(func):
        def wrapper(*args, **kwargs):
            with open(filename, "a") as file:
                file.write(f"{datetime.now()} {func.__name__} {args} {kwargs}\n")
            return func(*args, **kwargs)
        return wrapper
    return dec

@log_calls("log_calls.txt")
def f(name):
    a = input("Press F to pay respect: ")
    a.lower()
    if (a == "f"):
        print(f"{name}, you paid respect!")
    else:
        print("FAQ")

f("Алексей")