date = input("Введите дату(XX.XX): ").split(sep=".")
day = int(date[0])
month = int(date[1])

# Козерог
if (month == 12 and day >= 22) or (month == 1 and day <= 19):
    print("Козерог")
# Водолей
elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
    print("Водолей")
# Рыбы
elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
    print("Рыбы")
# Овен
elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
    print("Овен")
# Телец
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    print("Телец")
# Близнецы
elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
    print("Близнецы")
# Рак
elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
    print("Рак")
# Лев
elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    print("Лев")
# Дева
elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    print("Дева")
# Весы
elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
    print("Весы")
# Скорпион
elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
    print("Скорпион")
# Стрелец
elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
    print("Стрелец")