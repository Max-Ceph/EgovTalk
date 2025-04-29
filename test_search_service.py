from search_service import search_service_in_csv


def main():
    while True:
        query = input("\nВведите запрос для поиска (или 'exit' для выхода): ").strip()

        if query.lower() == "exit":
            print("Выход из программы.")
            break

        if not query:
            print("❗ Введите непустой запрос.")
            continue

        results = search_service_in_csv(query)

        if results:
            print(f"✅ Найдено {len(results)} результатов:")
            for service in results[:5]:  # Показываем максимум 5 результатов
                print(f"- {service['Услуга']} — {service['Ссылка']}")
        else:
            print("❌ Ничего не найдено по вашему запросу.")


if __name__ == "__main__":
    main()
