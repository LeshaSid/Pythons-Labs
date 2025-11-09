string = input("Введите список чисел через пробел: ")
ls_str = string.split()
if len(ls_str) < 2:
    print("Ошибка: нужно ввести хотя бы 2 числа")
else:
    ls = []
    for n in ls_str:
        if n.lstrip('-').replace('.', '', 1).isdigit():
            ls.append(float(n))
    if len(ls) < 2:
        print("Ошибка: после фильтрации осталось меньше 2 корректных чисел")
    else:
        ls.sort()
        print(f"Второе по величине число: {ls[-2]}")