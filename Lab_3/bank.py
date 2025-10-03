from random import randint
class Client:
    def __init__(self):
        full_name = input("ФИО: ")
        full_name = full_name.split()
        date_birth = input("Дата рождения: ")
        date_birth = int(date_birth.split())
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


