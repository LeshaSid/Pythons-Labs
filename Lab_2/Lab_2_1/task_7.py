s = input("Введите строку: ")

if not s:
    print("Ошибка! Пустая строка!")
else:
    new_s = ""
    count = 1
    
    for i in range(len(s)):
        if i < len(s) - 1 and s[i] == s[i + 1]:
            count += 1
        else:
            new_s += s[i] + str(count)
            count = 1
    
    print(f"Итоговая строка: {new_s}")