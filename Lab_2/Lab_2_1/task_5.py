str1 = input("Введите 1-ое слово: ").lower().replace(" ", "")
str2 = input("Введите 2-ое слово: ").lower().replace(" ", "")
is_anagram = True
if len(str1) != len(str2):
    is_anagram = False
else:
    sorted1 = sorted(str1)
    sorted2 = sorted(str2)
    
    for i in range(len(sorted1)):
        if sorted1[i] != sorted2[i]:
            is_anagram = False
            break
print(f"Анограмма? {is_anagram}")