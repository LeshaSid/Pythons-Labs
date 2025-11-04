string = input("Введите список через пробел: ")
ls = string.split()

unique_ls = []
for n in ls:
    if n not in unique_ls:
        unique_ls.append(n)

print(f"Без дубликатов: {unique_ls}")