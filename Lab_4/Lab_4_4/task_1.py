import pandas as pd 
import numpy as np 
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt 
from tabulate import tabulate
from sklearn.linear_model import LinearRegression

df_s7 = pd.read_excel("s7_data_sample_rev4_50k.xlsx", sheet_name="DATA")

rev_amount_sum = df_s7["REVENUE_AMOUNT"].sum()
rev_amount_mean = df_s7["REVENUE_AMOUNT"].mean()
rev_amount_median = df_s7["REVENUE_AMOUNT"].median()
rev_amount_max = df_s7["REVENUE_AMOUNT"].max()
rev_amount_min = df_s7["REVENUE_AMOUNT"].min()
rev_amount_std = df_s7["REVENUE_AMOUNT"].std()
print(f"""
Описательная статистика

Общая сумма выручки: {rev_amount_sum} руб
Средняя сумма выручки: {rev_amount_mean} руб
Медианная сумма выручки: {rev_amount_median} руб
Максимальное значение выручки: {rev_amount_max} руб
Минимальное значение выручки: {rev_amount_min} руб
Стандартное отклонение выручки: {rev_amount_std} руб
""")

plt.figure(figsize=(10, 8))
plt.hist(df_s7["REVENUE_AMOUNT"], bins=30)
plt.title("Гистограмма выручки")
plt.xlabel("Выручка (REVENUE_AMOUNT)")
plt.ylabel("Частота")
plt.grid(True)
plt.savefig("hist_revenue_amount.png") 
plt.close()

pax_counts = df_s7["PAX_TYPE"].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(pax_counts.values, labels=pax_counts.index, autopct="%1.1f%%")
plt.title("Круговая диаграмма по типам пассажиров")
plt.savefig("pie_pax_type.png") 
plt.close()

print("Топ 5 самых популярных аэропортов отправления")
top_orig = df_s7["ORIG_CITY_CODE"].value_counts().head(5).to_frame()
print(tabulate(top_orig, headers="keys", tablefmt="grid"))

print("\n\n")

print("Топ 5 самых популярных аэропортов назначения")
top_orig = df_s7["DEST_CITY_CODE"].value_counts().head(5).to_frame()
print(tabulate(top_orig, headers="keys", tablefmt="grid"))


df_s7['ISSUE_MONTH'] = pd.to_datetime(df_s7['ISSUE_DATE']).dt.month
df_s7['FLIGHT_MONTH'] = pd.to_datetime(df_s7['FLIGHT_DATE_LOC']).dt.month
monthly_sales = df_s7.groupby('ISSUE_MONTH')['REVENUE_AMOUNT'].sum()
monthly_count = df_s7.groupby('ISSUE_MONTH').size()

plt.figure(figsize=(10, 4))
plt.bar(monthly_sales.index, monthly_sales.values, color=["red", "green", "blue", "orange", "yellow", "purple", "lightblue", "lightgreen", "pink", "brown", "black", "indigo"])
plt.title('Выручка по месяцам продаж')
plt.xlabel('Месяц')
plt.ylabel('Выручка')
plt.grid(True)
plt.savefig("bar_monthes.png") 
plt.close()

print("\n\n")

stats = df_s7['FOP_TYPE_CODE'].value_counts().head(5).to_frame()
print("Топ-5 способов оплаты:")
print(tabulate(stats, headers="keys", tablefmt="grid"))

print("\nСредняя цена билета:")
for fop in stats.index[:3]:
    avg = df_s7[df_s7['FOP_TYPE_CODE'] == fop]['REVENUE_AMOUNT'].mean()
    print(f"{fop}: {avg:.0f} руб")


df_s7['DATE'] = pd.to_datetime(df_s7['ISSUE_DATE']).dt.date
daily = df_s7.groupby('DATE')['REVENUE_AMOUNT'].sum().reset_index()
daily['DATE_DT'] = pd.to_datetime(daily['DATE'])

daily['DAY_OF_WEEK'] = daily['DATE_DT'].dt.dayofweek
daily['IS_WEEKEND'] = (daily['DAY_OF_WEEK'] >= 5).astype(int)
daily['YESTERDAY'] = daily['REVENUE_AMOUNT'].shift(1)
daily = daily.dropna()

X = daily[['DAY_OF_WEEK', 'IS_WEEKEND', 'YESTERDAY']]
y = daily['REVENUE_AMOUNT']

splt_idx = int(len(daily) * 0.7)
X_train, X_test = X[:splt_idx], X[splt_idx:]
y_train, y_test = y[:splt_idx], y[splt_idx:]

model_l = LinearRegression()
model_l.fit(X_train, y_train)
score = model_l.score(X_test, y_test)

last_row = daily.iloc[-1]
tomorrow_day_of_week = (last_row['DAY_OF_WEEK'] + 1) % 7
tomorrow_is_weekend = 1 if tomorrow_day_of_week >= 5 else 0
yesterday_sales = last_row['REVENUE_AMOUNT']

tomorrow_features = pd.DataFrame(
    [[tomorrow_day_of_week, tomorrow_is_weekend, yesterday_sales]],
    columns=['DAY_OF_WEEK', 'IS_WEEKEND', 'YESTERDAY']
)

fut_pred = model_l.predict(tomorrow_features)[0]

print(f"""
Прогноз выручки на следующий день

Выручка завтра: {fut_pred:.2f} руб
Точность на тестовой выборке: {(score * 100):.0f} %
""")