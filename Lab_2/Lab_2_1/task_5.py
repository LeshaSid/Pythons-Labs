str1 = input("Введите 1-ое слово: ")
str2 = input("Введите 2-ое слово: ")
is_anagram = True
if (len(str1) == len(str2)):
    for i in str1:
        if i not in str2:
            is_anagram = False
            break
print(f"Анограмма? {is_anagram}")