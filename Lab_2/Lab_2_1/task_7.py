s = input("Введите строку: ")
new_s = ""
dict_s = {}
for i in s:
    dict_s[i] = dict_s.get(i, 0) + 1

for key in dict_s:
    new_s += str(key)
    new_s += str(dict_s[key])
print(f"Итоговая строка: {new_s}")