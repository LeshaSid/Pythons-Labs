zodiac_data = [
        ("Козерог", (12, 22, 1, 19)),
        ("Водолей", (1, 20, 2, 18)),
        ("Рыбы", (2, 19, 3, 20)),
        ("Овен", (3, 21, 4, 19)),
        ("Телец", (4, 20, 5, 20)),
        ("Близнецы", (5, 21, 6, 21)),
        ("Рак", (6, 22, 7, 22)),
        ("Лев", (7, 23, 8, 22)),
        ("Дева", (8, 23, 9, 22)),
        ("Весы", (9, 23, 10, 22)),
        ("Скорпион", (10, 23, 11, 21)),
        ("Стрелец", (11, 22, 12, 21))
    ]
date = input("Введите дату(XX.XX): ").split(sep=".")
for sign, (start_month, start_day, end_month, end_day) in zodiac_data:
        if (int(date[1]) == start_month and int(date[0]) >= start_day) or (int(date[1]) == end_month and int(date[0]) <= end_day):
            print(sign)

            