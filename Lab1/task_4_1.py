summ = int(input("Enter sum: "))
ls = [100, 50, 20, 10, 5, 2, 1]

print(str(100) + ": " + str(summ // 100))
summ -= 100*(summ // 100)

print(str(50) + ": " + str(summ // 50))
summ -= 50*(summ // 50)

print(str(20) + ": " + str(summ // 20))
summ -= 20*(summ // 20)

print(str(10) + ": " + str(summ // 10))
summ -= 10*(summ // 10)

print(str(5) + ": " + str(summ // 5))
summ -= 5*(summ // 5)

print(str(2) + ": " + str(summ // 2))
summ -= 2*(summ // 2)

print(str(1) + ": " + str(summ // 1))
summ -= 1*(summ // 1)