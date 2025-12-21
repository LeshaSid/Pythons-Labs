import pandas as pd 
from faker import Faker 
import random as rnd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fake = Faker("ru_RU")

form_of_education = ["очная", "заочная"]
specialization = ["радиофизика", "прикладная информатика", "кибербезопасность", "интеллектуальная электроника"]

def generate_student():
    score_lang = rnd.randint(0, 100)
    score_math = rnd.randint(0, 100)
    score_phys = rnd.randint(0, 100)
    avg_score_certificate = rnd.randint(20, 100) / 10.0
    total_score = score_lang + score_math + score_phys + avg_score_certificate * 10
    return {
        "name" : fake.name(),
        "year_of_admission" : rnd.randint(2021, 2025),
        "form_of_education" : rnd.choice(form_of_education),
        "score_lang" : score_lang,
        "score_math" : score_math,
        "score_phys" : score_phys,
        "avg_score_certificate" : avg_score_certificate,
        "total_score" : total_score,
        "specialization" : rnd.choice(specialization),
        "address" : fake.address(),
        "phone_number" : fake.phone_number()
    }

df = pd.DataFrame([generate_student() for i in range(1000)])

# Динамика среднего балла ЦТ/ЦЭ по предметам
plt.figure(figsize=(10, 6))
avg_scrcs_yrs = df.groupby("year_of_admission")[["score_lang", "score_math", "score_phys"]].mean()
years = [2021, 2022, 2023, 2024, 2025]
plt.plot(years, avg_scrcs_yrs.loc[years, "score_lang"], marker='o', label='Язык', linewidth=2, color="red")
plt.plot(years, avg_scrcs_yrs.loc[years, "score_math"], marker='s', label='Математика', linewidth=2, color="blue")
plt.plot(years, avg_scrcs_yrs.loc[years, "score_phys"], marker='^', label='Физика', linewidth=2, color="green")

plt.title('Динамика среднего балла ЦТ/ЦЭ по предметам')
plt.xlabel('Год поступления')
plt.ylabel('Средний балл')
plt.grid(True)
plt.legend(title='Предметы')
plt.xticks(years)

plt.tight_layout()
plt.savefig('dynamic_avg_score_exams_plot.png') 

# Динамика среднего балла аттестата
plt.figure(figsize=(10, 6))

avg_scores_by_year = df.groupby("year_of_admission")[["avg_score_certificate"]].mean()

plt.plot(years, avg_scores_by_year.loc[years, "avg_score_certificate"], label='Средний балл аттестата')
plt.title('Динамика среднего балла аттестата')
plt.xlabel('Год поступления')
plt.ylabel('Средний балл')
plt.grid(True)
plt.tight_layout()
plt.savefig('dynamic_avg_score_certificate_plot.png') 

# Динамика проходного балла
plt.figure(figsize=(10, 6))
avg_scores_by_year = df.groupby("year_of_admission")[["total_score"]].mean()

plt.barh(years, avg_scores_by_year.loc[years, "total_score"], label='Проходной балл', color=["red", "blue", "green", "orange", "purple"])
plt.title('Динамика проходного балла')
plt.ylabel('Год поступления')
plt.xlabel('Проходной балл')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('dynamic_total_score_plot.png')
plt.close()

# Количество студентов по специальностям
plt.figure(figsize=(10, 6))
specialization_cnts = df["specialization"].value_counts()
bars = plt.bar(specialization_cnts.index, specialization_cnts.values, 
               color=['red', 'blue', 'green', 'orange'])
plt.title('Количество студентов по специальностям')
plt.xlabel('Специальность')
plt.ylabel('Количество студентов')
plt.grid(True)
plt.tight_layout()
plt.savefig('specialization_count_plot.png')
plt.close()

# Распределение по формам обучения
plt.figure(figsize=(10, 6))
form_cnts = df["form_of_education"].value_counts()
plt.pie(form_cnts.values, labels=form_cnts.index, autopct='%1.1f%%', 
        colors=["red", "green"])
plt.title('Распределение по формам обучения')
plt.tight_layout()
plt.savefig('form_of_education_pie_plot.png')
plt.close()