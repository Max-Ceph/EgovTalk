#%%
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# ---------------- Скачивание стартовой страницы ----------------
def download_html(url, filename):
    if os.path.exists(filename):
        print(f"⚡ Файл {filename} уже существует. Пропускаем скачивание.")
        return

    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    with open(filename, "w", encoding="utf-8") as file:
        file.write(response.text)

    print(f"✅ Страница сохранена в {filename}")

# ---------------- Парсинг списка услуг ----------------
def parse_services(html_file, base_url):
    with open(html_file, encoding="utf-8") as file:
        soup = BeautifulSoup(file.read(), 'html.parser')

    services = []

    service_blocks = soup.select('div#region-frontpage-servs ul li a, div#region-frontpage-favs ul li a, div#region-content ul li a')

    for link in service_blocks:
        service_name = link.get_text(strip=True)
        service_href = link.get('href')

        if not service_href:
            continue

        if service_href.startswith("/"):
            service_href = base_url + service_href

        services.append({
            'Категория': '-',  # Заглушка (если нужно, можно доработать категорию отдельно)
            'Услуга': service_name,
            'Ссылка': service_href
        })

    return pd.DataFrame(services)

# ---------------- Парсинг "Результата оказания услуги" ----------------
def extract_service_result(url, result_keyword):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        blocks = soup.find_all('div', class_='info-block-horizontal')
        for block in blocks:
            title = block.find('p')
            if title and result_keyword in title.get_text(strip=True):
                return block.get_text(separator="\n", strip=True)

        return f"Раздел '{result_keyword}' не найден"
    except Exception as e:
        return f"Ошибка: {str(e)}"

# ---------------- Основная функция ----------------
def run_parser(start_page_url, html_file, result_file, result_keyword, base_url):
    print(f"\n🚀 Скачиваем и парсим: {start_page_url}")
    download_html(start_page_url, html_file)

    df = parse_services(html_file, base_url)

    results = []
    for _, row in df.iterrows():
        service = row['Услуга']
        link = row['Ссылка']
        result_text = extract_service_result(link, result_keyword)

        results.append({
            'Услуга': service,
            'Ссылка': link,
            'Результат оказания услуги': result_text
        })

    result_df = pd.DataFrame(results)
    result_df.to_csv(result_file, index=False, encoding="utf-8-sig")
    print(f"✅ Результаты сохранены в {result_file}")

# ---------------- Запуск для 3 языков ----------------
if __name__ == "__main__":
    run_parser(
        start_page_url="https://egov.kz/cms/ru/online-services/for_citizen",
        html_file="services_page_ru.html",
        result_file="services_with_results_ru.csv",
        result_keyword="Результат оказания услуги",
        base_url="https://egov.kz"
    )

    run_parser(
        start_page_url="https://egov.kz/cms/kk/online-services/for_citizen",
        html_file="services_page_kz.html",
        result_file="services_with_results_kz.csv",
        result_keyword="Қызмет көрсету нәтижесі",
        base_url="https://egov.kz"
    )

    run_parser(
        start_page_url="https://egov.kz/cms/en/online-services/for_citizen",
        html_file="services_page_en.html",
        result_file="services_with_results_en.csv",
        result_keyword="Result of the service delivery",
        base_url="https://egov.kz"
    )

    print("\n🌟 Готово: Все языковые версии обработаны!")
