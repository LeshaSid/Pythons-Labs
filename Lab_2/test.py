def type_checker(func):
    def wrapper(*args, **kwargs):
        if not isinstance(args[0], int) and not isinstance(args[0], float):
            print(f"На месте 1-го аргумента ожидался int/float, а был получен {type(args[0])}")
        if not isinstance(args[1], int) and not isinstance(args[1], float):
            print(f"На месте 2-го аргумента ожидался int/float, а был получен {type(args[1])}")
        if (isinstance(args[0], int) or isinstance(args[0], float)) and (isinstance(args[1], int) or isinstance(args[1], float)):
            if args[0] < 0:
                print(f"На месте 1-го аргумента ожидалось положительное число, а был получено отрицательное")
            if args[0] < 0:
                print(f"На месте 2-го аргумента ожидалось положительное число, а был получено отрицательное")
            else:
                result = func(*args, **kwargs)
                return result
        return None
    return wrapper

@type_checker
def pifagor(a, b):
    return (a**2 + b**2)**(1/2)

print(pifagor(3, 4))
print(pifagor(3.1, 2.3))
print(pifagor(3, "3"))
print(pifagor("2", "2"))
print(pifagor(-1, -3))
print(pifagor(1, -40))
print(pifagor(-3.1, -8.1))
print(pifagor([1, 2], 3))