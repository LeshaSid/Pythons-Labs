import pandas as pd 
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt 
from tabulate import tabulate
from sklearn.linear_model import LinearRegression

df = pd.read_csv('Ecommerce_Sales_Data_2024_2025.csv')
# https://www.kaggle.com/datasets/prince7489/e-commerce-sales

total_sales = df["Sales"].sum()
avg_sales = df["Sales"].mean()
total_profit = df["Profit"].sum()
avg_profit = df["Profit"].mean()
total_quantity = df["Quantity"].sum()
avg_price = (df["Sales"] / df["Quantity"]).mean()

print(f"""
Общая статистика продаж

Общая сумма продаж: {total_sales:.0f} рупий
Средняя сумма продаж: {avg_sales:.0f} рупий
Общая прибыль: {total_profit:.0f} рупий
Средняя прибыль: {avg_profit:.0f} рупий
Всего продано товаров: {total_quantity} шт
Средняя цена товара: {avg_price:.0f} рупий
""")

plt.figure(figsize=(10, 6))
plt.hist(df["Sales"], bins=30)
plt.title("Гистограмма продаж")
plt.xlabel("Сумма продажи (рупии)")
plt.ylabel("Частота")
plt.grid(True)
plt.savefig("hist_sales.png")
plt.close()

print("Топ 5 самых популярных категорий товаров:")
top_cats = df["Category"].value_counts().head(5).to_frame()
print(tabulate(top_cats, headers=["Категория", "Количество продаж"], tablefmt="grid"))

print("\nТоп 5 городов по продажам:")
top_cities = df["City"].value_counts().head(5).to_frame()
print(tabulate(top_cities, headers=["Город", "Количество заказов"], tablefmt="grid"))

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.year

monthly_sales = df.groupby('Month')['Sales'].sum()
monthly_count = df.groupby('Month').size()

plt.figure(figsize=(10, 4))
plt.bar(monthly_sales.index, monthly_sales.values, 
        color=["red", "green", "blue", "orange", "yellow", "purple", 
               "lightblue", "lightgreen", "pink", "brown", "black", "indigo"])
plt.title('Продажи по месяцам')
plt.xlabel('Месяц (1-12)')
plt.ylabel('Продажи (рупии)')
plt.grid(True)
plt.savefig("bar_monthly_sales.png")
plt.close()

print("\nСпособы оплаты:")
payment_stats = df['Payment Mode'].value_counts().to_frame()
print(tabulate(payment_stats, headers=["Способ оплаты", "Количество"], tablefmt="grid"))

print("\nСредняя сумма по способам оплаты:")
for pay in payment_stats.index:
    avg = df[df['Payment Mode'] == pay]['Sales'].mean()
    print(f"{pay}: {avg:.0f} рупий")

df['Date'] = pd.to_datetime(df['Order Date']).dt.date
daily = df.groupby('Date')['Sales'].sum().reset_index()
daily['Date_dt'] = pd.to_datetime(daily['Date'])

daily['Day_of_Week'] = daily['Date_dt'].dt.dayofweek
daily['Is_Weekend'] = (daily['Day_of_Week'] >= 5).astype(int)
daily['Sales_Lag1'] = daily['Sales'].shift(1)
daily['Sales_MA_7'] = daily['Sales'].rolling(window=7, min_periods=1).mean()
daily['Last_Week_Same_Day'] = daily['Sales'].shift(7)
daily = daily.dropna()

X = daily[['Day_of_Week', 'Is_Weekend', 'Sales_Lag1', 'Sales_MA_7', 'Last_Week_Same_Day']]
y = daily['Sales']

split_idx = int(len(daily) * 0.7)
X_train, X_test = X[:split_idx], X[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]

model = LinearRegression()
model.fit(X_train, y_train)
score = model.score(X_test, y_test)

last_row = daily.iloc[-1]

tomorrow_day = (last_row['Day_of_Week'] + 1) % 7
tomorrow_weekend = 1 if tomorrow_day >= 5 else 0
yesterday_sales = last_row['Sales']
ma_7 = last_row['Sales_MA_7']
last_week_same_day = daily.iloc[-7]['Sales'] if len(daily) >= 7 else ma_7

tomorrow_features = pd.DataFrame(
    [[tomorrow_day, tomorrow_weekend, yesterday_sales, ma_7, last_week_same_day]],
    columns=['Day_of_Week', 'Is_Weekend', 'Sales_Lag1', 'Sales_MA_7', 'Last_Week_Same_Day']
)

tomorrow_pred = model.predict(tomorrow_features)[0]

print(f"""
Прогноз продаж на следующий день

Продажи завтра: {tomorrow_pred:.0f} рупий
Точность прогноза: {(score * 100):.0f}%
""")

category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 8))
plt.pie(category_sales.values[:10], 
        labels=category_sales.index[:10], 
        autopct='%1.1f%%',
        startangle=90)
plt.title('Продажи по категориям (топ-10)')
plt.savefig("pie_categories.png")
plt.close()

plt.figure(figsize=(12, 5))
plt.plot(daily['Date'], daily['Sales'])
plt.title('Динамика продаж по дням')
plt.xlabel('Дата')
plt.ylabel('Продажи (рупии)')
plt.grid(True)
plt.savefig("line_daily_sales.png")
plt.close()

max_sale_idx = df['Sales'].idxmax()
expensive_item = df.loc[max_sale_idx, 'Product Name']
expensive_price = df.loc[max_sale_idx, 'Sales']
print(f"Самый дорогой товар: {expensive_item}")
print(f"Стоимость: {expensive_price:.0f} рупий")

max_profit_idx = df['Profit'].idxmax()
profit_item = df.loc[max_profit_idx, 'Product Name']
profit_amount = df.loc[max_profit_idx, 'Profit']
print(f"\nСамый прибыльный товар: {profit_item}")
print(f"Прибыль: {profit_amount:.0f} рупий")

print("\nСредние продажи по регионам:")
for region in df['Region'].unique():
    avg = df[df['Region'] == region]['Sales'].mean()
    print(f"{region}: {avg:.0f} рупий")