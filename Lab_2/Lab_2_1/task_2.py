string = input("Введите список чисел через пробел: ")
ls_str = string.split()
ls = []
for n in ls_str:
    ls.append(float(n))
    
unique_numbers = []
for n in ls:
    if ls.count(n) == 1:
        unique_numbers.append(n)
print(f"Уникальные числа: {unique_numbers}")

repeating_numbers = []
for n in ls:
    if ls.count(n) > 1 and n not in repeating_numbers: 
        repeating_numbers.append(n)
print(f"Повторяющиеся числа: {repeating_numbers}")

even_numbers = []
odd_numbers = []
for n in ls:
    if n == int(n):
        if n % 2 == 0:
            even_numbers.append(n)
        else:
            odd_numbers.append(n)
print(f"Четные числа: {even_numbers}")
print(f"Нечетные числа: {odd_numbers}")

negative_numbers = []
for n in ls:
    if n < 0:
        negative_numbers.append(n)
print(f"Отрицательные числа: {negative_numbers}")

float_numbers = []
for n in ls:
    if n != int(n):
        float_numbers.append(n)
print(f"Числа с плавающей точкой: {float_numbers}")

sum_mult_5 = 0
for n in ls:
    if n % 5 == 0:
        sum_mult_5 += n
print(f"Сумма всех чисел, кратных 5: {sum_mult_5}")

print(f"Самое большое число: {max(ls)}")
print(f"Самое маленькое число: {min(ls)}")