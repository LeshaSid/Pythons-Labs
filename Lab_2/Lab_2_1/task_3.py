string = input("Введите список чисел через пробел: ")
ls_str = string.split()
ls = []
for n in ls_str:
    ls.append(int(n))
ls.sort()
print(f"Второе по величине число: {ls[-2]}")