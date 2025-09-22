summ = int(input("Enter sum: "))
ls = [100, 50, 20, 10, 5, 2, 1]
for i in ls:
    print(str(i) + ": " + str(summ // i))
    summ -= i*(summ // i)