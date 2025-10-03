string = input("Введите 1-ый список чисел через пробел: ")
ls_str = string.split()
ls1 = []
for n in ls_str:
    ls1.append(int(n))

string = input("Введите 2-ой список чисел через пробел: ")
ls_str = string.split()
ls2 = []
for n in ls_str:
    ls2.append(int(n))

ls = ls1 + ls2
both = []
for n in ls:
    if ls.count(n) > 1 and n not in both: 
        both.append(n)
print(f"Числа, которые присутствуют в обоих наборах одновременно: {both}")

not_in_1 = []
not_in_2 = []
for n in ls1:
    if n not in ls2:
        not_in_2.append(n)
for n in ls2:
    if n not in ls1:
        not_in_1.append(n)
print(f"Числа из первого набора, которые отсутствуют во втором: {not_in_2}")
print(f"Числа из второго набора, которые отсутствуют в первом: {not_in_1}")

exceptions = []
for n in ls:
    if n not in both:
        exceptions.append(n)
print(f"Числа из обоих наборов, за исключением чисел, найденных в пункте 1: {not_in_1}")      
