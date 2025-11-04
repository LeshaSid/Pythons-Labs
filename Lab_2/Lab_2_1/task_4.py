ls_str_1 = input("Введите 1-ый список чисел через пробел: ")
ls1 = [float(n) for n in ls_str_1.split()]

ls_str_2 = input("Введите 2-ой список чисел через пробел: ")
ls2 = [float(n) for n in ls_str_2.split()]

set1 = set(ls1)
set2 = set(ls2)
both = set1 & set2
print(f"Числа, которые присутствуют в обоих наборах одновременно: {both}")

not_in_2 = set1 - set2
not_in_1 = set2 - set1
print(f"Числа из первого набора, которые отсутствуют во втором: {not_in_2}")
print(f"Числа из второго набора, которые отсутствуют в первом: {not_in_1}")

exceptions = (set1 | set2) - set(both)
print(f"Числа из обоих наборов, за исключением чисел, найденных в пункте 1: {exceptions}")      
