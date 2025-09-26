a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(str(a) + " + " + str(b) + " = " + str(a+b))
print(str(a) + " - " + str(b) + " = " + str(a-b))
print(str(a) + " * " + str(b) + " = " + str(a*b))
if (b == 0):
    print("На ноль делить нельзя!")
else:
    print(str(a) + " / " + str(b) + " = " + str(a/b))
    print("Остаток от деления " + str(a) + " на " + str(b) + " = " + str(a%b))
print(str(a) + " ^ " + str(b) + " = " + str(a**b))