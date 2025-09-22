n = int(input("Enter num: "))
if n % 7 == 0:
    print("Магическое число")
else:
    sum_dig = 0
    while n != 0:
        sum_dig += n % 10
        n = n // 10
    print("Sum of digits = " + str(sum_dig))