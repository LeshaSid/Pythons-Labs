password = input("Введите пароль: ")
if len(password) > 16:
    if password.isalpha() or password.isdigit():
        print("Слабый пароль")
    else:
        print("Надёжный пароль")
else:
    print("Слишком короткий")