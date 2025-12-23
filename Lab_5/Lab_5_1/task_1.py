import requests
from bs4 import BeautifulSoup
import csv
import time
import os
import argparse
import re

INPUT_FILE = 'countries.txt'
OUTPUT_FILE = 'countries_data.csv'
CACHE = 'cache_pages'

parser = argparse.ArgumentParser()
parser.add_argument('--input', default=INPUT_FILE)
parser.add_argument('--output', default=OUTPUT_FILE)
args = parser.parse_args()

def get_page(country):
    if not os.path.exists(CACHE):
        os.makedirs(CACHE)
    path = os.path.join(CACHE, country.replace(' ', '_') + ".html")
    if os.path.exists(path):
        return open(path, 'r', encoding='utf-8').read()
    
    print(f"Загрузка: {country}...")
    url = f"https://en.wikipedia.org/wiki/{country.replace(' ', '_')}"
    try:
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        r.raise_for_status()
        with open(path, 'w', encoding='utf-8') as f:
            f.write(r.text)
        time.sleep(1)
        return r.text
    except Exception:
        return None

def extract_number(text):
    if not text:
        return "N/A"

    text = re.sub(r'\[.*?\]', '', text).replace(',', '').replace('\xa0', '').strip()
    match = re.search(r'\d+', text)
    return match.group(0) if match else "N/A"

if not os.path.exists(args.input):
    print("Создай файл countries.txt!")
    exit()

with open(args.input, 'r', encoding='utf-8') as f:
    countries = [line.strip() for line in f if line.strip()]

results = []

for c in countries:
    html = get_page(c)
    if not html: 
        continue

    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', {'class': 'infobox'})
    if not table:
        continue

    res = {'country': c, 'city': 'N/A', 'area': 'N/A', 'population': 'N/A'}
    
    rows = table.find_all('tr')
    for i, row in enumerate(rows):
        th = row.find('th')
        td = row.find('td')
        if not th:
            continue
        
        txt = th.get_text().lower()

        if 'capital' in txt and td:
            link = td.find('a')
            res['city'] = link.get_text() if link else td.get_text().split('[')[0].strip()

        if 'area' in txt:
            for j in range(i, i + 3):
                if j < len(rows):
                    curr_td = rows[j].find('td')
                    curr_th = rows[j].find('th')
                    if curr_td and any(d.isdigit() for d in curr_td.get_text()):
                        if j == i or (curr_th and 'total' in curr_th.get_text().lower()):
                            res['area'] = extract_number(curr_td.get_text())
                            break

        if 'population' in txt:
            for j in range(i + 1, i + 5):
                if j < len(rows):
                    curr_th = rows[j].find('th')
                    curr_td = rows[j].find('td')
                    if curr_td and any(d.isdigit() for d in curr_td.get_text()):
                        header_sub = curr_th.get_text().lower() if curr_th else ""
                        if any(x in header_sub for x in ['estimate', 'census', 'total']) or not curr_th:
                            res['population'] = extract_number(curr_td.get_text())
                            break

    print(f"{c}, {res['city']}, {res['area']}, {res['population']}")
    results.append(res)

with open(args.output, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['country', 'city', 'area', 'population'])
    w.writeheader()
    w.writerows(results)