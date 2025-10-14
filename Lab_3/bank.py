from random import randint
global clt_ids, exchange_rate
clt_ids = []
exchange_rate = {}

class Account:
    def __init__(self, currency, balance=0):
        self.currency = currency
        self.balance = balance

class Bank:
    def __init__(self, bank_name):
        self.name = bank_name
        self.clients = {}
        self.accounts = {}

class Client:
    def __init__(self, client_id, full_name, date_birth):
        self.full_name = input("ФИО: ")
        self.date_birth = input("Дата рождения: ")
        
        is_unique_id = False
        while not is_unique_id:
            self.id = "CLT" + str(randint(10, 99)) + chr(randint(65, 90)) + str(randint(1000, 9999))
            if self.id not in clt_ids:
                clt_ids.append(self.id)
                is_unique_id = True
                print(f"Ваш ID: {self.id}")
        
        self.accounts = {}

    def open_account(self, currency):
        if currency in self.accounts:
            raise ValueError(f"Счет в валюте {currency} уже существует")
        
        self.accounts[currency] = Account(currency)
        print(f"Счет в валюте {currency} успешно открыт")

    def close_account(self, currency):
        if currency not in self.accounts:
            raise ValueError(f"Счет в валюте {currency} не существует")
        
        if self.accounts[currency].balance != 0:
            raise ValueError("Нельзя закрыть счет с ненулевым балансом")
        
        del self.accounts[currency]
        print(f"Счет в валюте {currency} успешно закрыт")

    def deposit(self, currency, amount):
        if currency not in self.accounts:
            raise ValueError(f"Счет в валюте {currency} не существует")
        
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        
        self.accounts[currency].balance += amount
        print(f"Счет пополнен на {amount:.2f} {currency}.\n Новый баланс: {self.accounts[currency].balance:.2f}")

    def withdraw(self, currency, amount):
        if currency not in self.accounts:
            raise ValueError(f"Счет в валюте {currency} не существует")
        
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        
        if amount > self.accounts[currency].balance:
            raise ValueError("Недостаточно средств на счете")
        
        self.accounts[currency].balance -= amount
        print(f"Со счета снято {amount:.2f} {currency}.\n Новый баланс: {self.accounts[currency].balance:.2f}")

    def transfer(self, from_currency, to_currency, amount, to_client=None):
        if to_client is None:
            to_client = self
        
        if from_currency not in self.accounts:
            raise ValueError(f"Исходный счет в валюте {from_currency} не существует")
        
        if to_currency not in to_client.accounts:
            raise ValueError(f"Целевой счет в валюте {to_currency} не существует")
        
        if amount <= 0:
            raise ValueError("Сумма перевода должна быть положительной")
        
        if amount > self.accounts[from_currency].balance:
            raise ValueError("Недостаточно средств на исходном счете")
        
        self.accounts[from_currency].balance -= amount
        to_client.accounts[to_currency].balance += amount
        
        if to_client == self:
            print(f"Переведено {amount:.2f} {from_currency} → {to_currency}. Перевод между своими счетами.")
        else:
            print(f"Переведено {amount:.2f} {from_currency} → {to_currency} клиенту {to_client.full_name}")


class Main:
    def __init__(self):
        self.bank = Bank("MyBank")
        self.current_client = None

    def main():
        user_id = input("Введите ваш ID: ")
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


if __name__ == "__main__":
    app = Main()
    app.main()