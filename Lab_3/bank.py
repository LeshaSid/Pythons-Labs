from random import randint
global ids
ids = []

class Client:
    def __init__(self):
        full_name = input("ФИО: ")
        full_name = full_name.split()
        date_birth = input("Дата рождения: ")
        date_birth = int(date_birth.split())
        is_unique_id = False
        while not is_unique_id:
            id = chr(randint(65, 90)) + chr(randint(65, 90)) + str(randint(1000000, 9999999))
            if id in ids:
                is_unique_id = True
        

    def open(self, name_of_account):
        pass
    def close(self, name_of_account):
        pass
    def deposit(self, name_of_account, amount):
        pass
    def withdraw(self, amount):
        pass
    def transfer(self):
        pass


class Account:
    def __init__(self):
        currency = input("Введите валюту счёта: ")
        balance = int(input("Введите начальный баланс: "))

    
class Bank:
    def __init__(self, bank_name):
        pass

class Main:
    def main():
        user_id = input()
        while True:
            print("""1. Открыть счет для клиента. 
                    2. Закрыть счет клиента. 
                    3. Пополнить банковский счет.
                    4. Снять сумму со счета.
                    5. Перевести деньги между счетами.""")
            ans = int(input())
            if ans == 1:
                pass
            elif ans == 2:
                pass
            elif ans == 3:
                pass
            elif ans == 4:
                pass
            elif ans == 5:
                pass
            else:
                pass
