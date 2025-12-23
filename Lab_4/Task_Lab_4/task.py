# магазины музыкальных инструментов название, адрес,
# колличество реализованной продукции, сумма реализованной продукции, средняя цена покупки, визуализация
import pandas as pd 
from faker import Faker 
from faker_music import MusicProvider
import matplotlib.pyplot as plt

fake = Faker("ru_RU")
fake.add_provider(MusicProvider)

def generate_market():
    amount_of_products = fake.random_int(min=1, max=1000)
    sum_of_products = fake.random_int(min=20, max=500000)
    avg_price = sum_of_products / amount_of_products
    name_market = [fake.music_genre(), fake.music_subgenre(), fake.music_instrument()]
    return {
        "name" : fake.random.choice(name_market) + " Market",
        "address" : fake.address(),
        "year_create" : fake.date(pattern="%Y"),
        "category" : fake.music_instrument_category(),
        "amount_of_products" : amount_of_products,
        "sum_of_products" : sum_of_products,
        "avg_price" : avg_price
    }

mus_markets_df = pd.DataFrame([generate_market() for i in range(1000)])
print(f"""
Описательная статистика

Общее колличество покупок: {mus_markets_df["amount_of_products"].sum()} шт
Общаяя сумма покупок: {mus_markets_df["sum_of_products"].sum()} руб
Средняя цена покупки: {mus_markets_df["avg_price"].mean()} руб
Медианная цена покупки: {mus_markets_df["avg_price"].mean()} руб
""")


plt.figure(figsize=(10, 8))
plt.hist(mus_markets_df["sum_of_products"], bins=30)
plt.title("Гистограмма суммы реализованной продукции")
plt.xlabel("Сумма реализованной продукции")
plt.ylabel("Частота")
plt.grid(True)
plt.savefig("hist_sum_of_products.png") 
plt.close()

plt.figure(figsize=(10, 8))
plt.hist(mus_markets_df["amount_of_products"], bins=30)
plt.title("Гистограмма количества реализованной продукции")
plt.xlabel("Сумма реализованной продукции")
plt.ylabel("Частота")
plt.grid(True)
plt.savefig("hist_amount_of_products.png") 
plt.close()

print("\nТоп 5 магазинов по сумме продаж")
top_sum_of_products = mus_markets_df.sort_values(by="sum_of_products", ascending=False).head(5)
print(top_sum_of_products[["name", "sum_of_products"]])
print("\n")
print("\nТоп 5 магазинов по колличеству продаж")
top_amount_of_products = mus_markets_df.sort_values(by="amount_of_products", ascending=False).head(5)
print(top_sum_of_products[["name", "amount_of_products"]])
print("\n")
print("\nТоп 5 магазинов по средней цене")
top_avg_price = mus_markets_df.sort_values(by="avg_price", ascending=False).head(5)
print(top_avg_price[["name", "avg_price"]])

category = mus_markets_df.groupby("category")["amount_of_products"].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 8))
plt.pie(category.values, 
        labels=category.index, 
        autopct='%1.1f%%')
plt.title("Категории магазинов")
plt.savefig("pie_category.png") 
plt.close()

price_category = mus_markets_df.groupby("category")["amount_of_products"].sum()
plt.figure(figsize=(10, 8))
plt.bar(price_category.index, price_category.values, 
        color=["red", "green", "blue", "orange"])
plt.title("Наибольшее колличество проданных товаров по категориям магазинов")
plt.savefig("bar_category.png") 
plt.close()

yearly = mus_markets_df.groupby("year_create")["sum_of_products"].sum().reset_index()
plt.figure(figsize=(30, 10))
plt.plot(yearly["year_create"], yearly["sum_of_products"])
plt.title("График зависимости суммы реализованной продукции от даты создания магазина")
plt.xlabel("Дата создания")
plt.ylabel("Сумма реализованной продукции")
plt.grid(True)
plt.savefig("plot_year.png")
plt.close()

