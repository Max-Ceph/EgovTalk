import pandas as pd
import pymorphy2

morph = pymorphy2.MorphAnalyzer()

DATA_FILE = "services_with_results.csv"

df = pd.read_csv(DATA_FILE)

def lemmatize(text):
    return ' '.join(morph.parse(word)[0].normal_form for word in str(text).lower().split())

df["lemma_Услуга"] = df["Услуга"].apply(lemmatize)
df["lemma_Категория"] = df["Категория"].apply(lemmatize)
df["lemma_Результат"] = df["Результат оказания услуги"].apply(lemmatize)

def search_service_in_csv(query):
    query_lemma = lemmatize(query.lower())

    # 1. Поиск по названию услуги
    res_1 = df[df['lemma_Услуга'].str.contains(query_lemma, na=False)]

    # 2. Поиск по категории, исключая уже найденные
    res_2 = df[
        df['lemma_Категория'].str.contains(query_lemma, na=False) &
        ~df.index.isin(res_1.index)
    ]

    # 3. Поиск по результату, исключая уже найденные
    res_3 = df[
        df['lemma_Результат'].str.contains(query_lemma, na=False) &
        ~df.index.isin(res_1.index) &
        ~df.index.isin(res_2.index)
    ]

    # Объединение всех результатов с приоритетом
    results = pd.concat([res_1, res_2, res_3])

    return results.to_dict(orient="records")
