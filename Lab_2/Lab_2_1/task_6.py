string = input("Введите список через пробел: ")
ls = string.split()

unique_numbers = []
for n in ls:
    if ls.count(n) == 1:
        unique_numbers.append(n)
print(f"Без дубликатов': {unique_numbers}")