from random import randint

global clt_ids, exchange_rate, banks
clt_ids = []
exchange_rates = {
    "USD": 1.0,
    "EUR" : 0.87,
    "BYN" : 2.98,
    "RUB" : 80.84,
    "PLN" : 3.71,
    "CNY" : 7.12
    
}
banks = {}

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

class Client:
    def __init__(self, full_name, date_birth):
        self.full_name = full_name
        self.date_birth = date_birth
        
        is_unique_id = False
        while not is_unique_id:
            self.id = ("CLT" + str(randint(0, 9)) + str(randint(0, 9))
                        + chr(randint(65, 90)) + str(randint(0, 9)) +
                        str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)))
            if self.id not in clt_ids:
                clt_ids.append(self.id)
                is_unique_id = True
                print(f"{self.full_name}, ваш ID: {self.id}")
        
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

    def transfer(self, from_currency, to_currency, amount, to_client_id=None, to_bank_name=None, bank=None):
        if from_currency not in self.accounts:
            raise ValueError(f"Исходный счет в валюте {from_currency} не существует")
        
        if amount <= 0:
            raise ValueError("Сумма перевода должна быть положительной")
        
        if amount > self.accounts[from_currency].balance:
            raise ValueError("Недостаточно средств на исходном счете")
        
        if to_client_id is None:
            if to_currency not in self.accounts:
                raise ValueError(f"Целевой счет в валюте {to_currency} не существует")
            
            self.accounts[from_currency].balance -= amount
            self.accounts[to_currency].balance += convert_currency(amount, from_currency, to_currency)
            print(f"Переведено {amount:.2f} {from_currency} → {to_currency}. Перевод между своими счетами.")
        else:
            if to_bank_name is None:
                raise ValueError("Не указан банк получателя")
            
            if to_bank_name not in banks:
                raise ValueError(f"Банк {to_bank_name} не существует")
            
            to_bank = banks[to_bank_name]
            if to_client_id not in to_bank.clients:
                raise ValueError("Клиент-получатель не найден в указанном банке")
            
            to_client = to_bank.clients[to_client_id]
            if to_currency not in to_client.accounts:
                raise ValueError(f"Целевой счет в валюте {to_currency} не существует у получателя")
            
            converted_amount = convert_currency(amount, from_currency, to_currency)
            commission_amount = converted_amount * bank.commission
            final_amount = converted_amount - commission_amount
            
            self.accounts[from_currency].balance -= amount
            to_client.accounts[to_currency].balance += final_amount
            
            print(f"Переведено {amount:.2f} {from_currency} → {to_currency} клиенту {to_client.full_name}")
            print(f"Комиссия банка: {commission_amount:.2f} {to_currency}")

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

class Bank:
    def __init__(self, bank_name, commission):
        self.name = bank_name
        self.commission = commission
        self.clients = {}
        self.accounts = {}

    def add(self, client):
        self.clients[client.id] = client
        self.accounts[client.id] = client.accounts
    
    def delete(self, client):
        if client.id in self.clients:
            del self.clients[client.id]
            del self.accounts[client.id]    
    

class Main:
    def main(self):
        bank1 = Bank("ФПИ Банк", 0.02)
        bank2 = Bank("Грэйс", 1.02)
        client1 = Client("Сидорук Алексей Александрович", "01.02.2006")
        client2 = Client("Данилова Антонина Дмитриевна", "26.07.2006")
        client3 = Client("Хомич Степан Юрьевич", "13.06.2006")
        bank1.add(client1)
        bank1.add(client2)
        bank2.add(client3)
        banks[bank1.name] = bank1
        banks[bank2.name] = bank2

        while True:
            ans = int(input("1. Выбрать банк\n2. Выйти\n"))
            if ans == 1:
                bank_name = input(f"Выберите банк {tuple(banks.keys())[::]}: ")
                if bank_name in banks:
                    bank = banks[bank_name]
                    user_id = input("Введите ваш ID: ")
                    if (user_id in clt_ids) and (user_id in bank.clients):
                        current_client = bank.clients[user_id]
                        while True:
                            print("""1. Открыть счет для клиента.
2. Закрыть счет клиента. 
3. Пополнить банковский счет. 
4. Снять сумму со счета.
5. Перевести деньги между своими счетами.
6. Перевести деньги на счёт другого клиента.
7. Сделать выписку по счетам.
8. Выход.""")
                            ans = int(input())
                            if ans == 1:
                                cur = input(f"Введите валюту для счёта{tuple(exchange_rates.keys())[::]}: ")
                                current_client.open_account(cur)
                            elif ans == 2:
                                cur = input("Введите валюту для счёта: ")
                                current_client.close_account(cur)
                            elif ans == 3:
                                cur = input("Введите валюту для счёта: ")
                                am = int(input("Введите сумму пополнения: "))
                                current_client.deposit(cur, am)
                            elif ans == 4:
                                cur = input("Введите валюту для счёта: ")
                                am = int(input("Введите сумму пополнения: "))
                                current_client.withdraw(cur, am) 
                            elif ans == 5:
                                from_cur = input("Введите валюту исходного счёта: ")
                                to_cur = input("Введите валюту счёта-получателя: ")
                                am = int(input("Введите сумму перевода: "))
                                current_client.transfer(from_cur, to_cur, am)
                            elif ans == 6:
                                to_clt = input("Введите ID клиента-получателя: ")
                                to_bank = input("Введите название банка получателя: ")
                                from_cur = input("Введите валюту исходного счёта: ")
                                to_cur = input("Введите валюту счёта-получателя: ")
                                am = int(input("Введите сумму перевода: "))
                                current_client.transfer(from_cur, to_cur, am, to_clt, to_bank, bank)
                            elif ans == 7:
                                current_client.account_statement()
                                print("Выписка по всем счетам сделана!")
                            elif ans == 8:
                                break
                            else:
                                raise ValueError("Пункта меню с таким номером не существует!")
                    else:
                        raise ValueError("Клиента с таким ID не существует!")
                else:
                    raise ValueError(f"Банка {bank} не существует!")           
            elif ans == 2:
                break
            else:
                raise ValueError("Пункта меню с таким номером не существует!")


if __name__ == "__main__":
    app = Main()
    app.main()