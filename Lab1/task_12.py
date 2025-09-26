minutes = float(input("Минуты разговора: "))
sms = float(input("Количество СМС: "))
internet = float(input("Интернет(Мб): "))

print("Сумма тарификации: 24.99 руб")

addit_int = 0
addit_min = 0
addit_sms = 0

if minutes > 60:
    addit_min = minutes - 60
    print("Сумма за дополнительные минуты: " + str(round((addit_min * 0.89), 2)) + " руб")

if sms > 30:
    addit_sms = sms - 30
    print("Сумма за дополнительные сообщения: " + str(round((addit_sms * 0.59), 2)) + " руб")  # Исправлено: addit_sms

if internet > 1024:
    addit_int = internet - 1024
    print("Сумма за дополнительный интернет-трафик: " + str(round((addit_int * 0.79), 2)) + " руб")  # Исправлено: addit_int

sum_services = 24.99 + addit_min * 0.89 + addit_sms * 0.59 + addit_int * 0.79
tax = round((sum_services) * 0.02, 2)
total = round(sum_services + tax, 2)

print("Налог: " + str(tax) + " руб")
print("Итоговая сумма: " + str(total) + " руб")