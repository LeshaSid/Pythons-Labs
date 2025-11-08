from random import randint

global clt_ids, exchange_rate
clt_ids = []
exchange_rates = {
    "USD": 1.0,
    "EUR" : 0.87,
    "BYN" : 2.98,
    "RUB" : 80.84,
    "PLN" : 3.71,
    "CNY" : 7.12
    
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        raise ValueError("Валюта не найдена в словаре")
    
    amount_in_usd = amount / exchange_rates[from_currency]
    converted_amount = amount_in_usd * exchange_rates[to_currency]
    
    return round(converted_amount, 2)

class Account:
    def __init__(self, currency, balance=0):
        self.currency = currency
        self.balance = balance

class Bank:
    def __init__(self, bank_name):
        self.name = bank_name
        self.clients = {}
        self.accounts = {}

    def add(self, client):
        self.clients[client.id] = client
        self.accounts[client.id] = client.accounts
    
    def delete(self, client):
        self.clients.popitem(client.id)
        self.accounts.popitem(client.id)

class Client:
    def __init__(self, full_name, date_birth):
        self.full_name = full_name
        self.date_birth = date_birth
        
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
        if currency not in exchange_rates:
            raise ValueError(f"Невозможно создать счёт в валюте {currency}")
        
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
        to_client.accounts[to_currency].balance += convert_currency(amount, from_currency, to_currency)
        
        if to_client == self:
            print(f"Переведено {amount:.2f} {from_currency} → {to_currency}. Перевод между своими счетами.")
        else:
            print(f"Переведено {amount:.2f} {from_currency} → {to_currency} клиенту {to_client.full_name}")

    def account_statement(self):
        with open("statement.txt", "w") as file:
            file.write(f"ID: {self.id}\n")
            file.write(f"ФИО: {self.full_name}\n")
            file.write(f"Дата рождения: {self.date_birth}\n")
            amount_all_acc = 0
            for acc in self.accounts:
                file.write(f"Остаток на счету в валюте {acc}: {self.accounts[acc].balance} {acc}\n")
                amount_all_acc += convert_currency(self.accounts[acc].balance, acc, "USD")
            file.write(f"Сумма на всех счетах {amount_all_acc} USD\n")
            


class Main:
    def __init__(self):
        self.bank = Bank("MyBank")
        self.current_client = Client("Сидорук Алексей Александрович", "01.02.2006")

    def main(self):
        user_id = input("Введите ваш ID: ")
        if user_id in clt_ids:
            while True:
                print("""1. Открыть счет для клиента.
2. Закрыть счет клиента. 
3. Пополнить банковский счет. 
4. Снять сумму со счета.
5. Перевести деньги между счетами.
6. Сделать выписку по счетам
7. Выход""")
                ans = int(input())
                if ans == 1:
                    cur = input(f"Введите валюту для счёта{tuple(exchange_rates.keys())[::]}: ")
                    self.current_client.open_account(cur)
                elif ans == 2:
                    cur = input("Введите валюту для счёта: ")
                    self.current_client.close_account(cur)
                elif ans == 3:
                    cur = input("Введите валюту для счёта: ")
                    am = int(input("Введите сумму пополнения: "))
                    self.current_client.deposit(cur, am)
                elif ans == 4:
                    cur = input("Введите валюту для счёта: ")
                    am = int(input("Введите сумму пополнения: "))
                    self.current_client.withdraw(cur, am) 
                elif ans == 5:
                    from_cur = input("Введите валюту исходного счёта: ")
                    to_cur = input("Введите валюту счёта-получателя: ")
                    am = int(input("Введите сумму перевода: "))
                    self.current_client.transfer(from_cur, to_cur, am)
                elif ans == 6:
                    self.current_client.account_statement()
                    print("Выписка по всем счетам сделана!")
                elif ans == 7:
                    False
                else:
                    raise ValueError("Пункта меню с таким номером не существует!")
        else:
            raise ValueError("Клиента с таким ID не существует!")


if __name__ == "__main__":
    app = Main()
    app.main()