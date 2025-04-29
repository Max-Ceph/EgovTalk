import pandas as pd

DATA_FILE = "services_with_results.csv"
df = pd.read_csv(DATA_FILE)

def search_service_in_csv(query):
    query = query.lower()
    results = df[
        df['Услуга'].str.lower().str.contains(query, na=False) |
        df['Категория'].str.lower().str.contains(query, na=False) |
        df['Результат оказания услуги'].str.lower().str.contains(query, na=False)
    ]
    return results.to_dict(orient="records")
