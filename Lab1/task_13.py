from random import randint
num = randint(1, 100)
ans = False
while (ans == False):
    x = int(input("Введите число: "))
    if (x > num):
        print("Меньше")
    elif (x < num):
        print("Больше")
    else:
        print("Верно!")
        ans = True
