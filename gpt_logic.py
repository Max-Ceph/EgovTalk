import os
from openai import OpenAI
from dotenv import load_dotenv
from search_service import search_service_in_csv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_query_with_gpt(user_query: str) -> str:
    results = search_service_in_csv(user_query)

    if not results:
        return "⚠️ По вашему запросу ничего не найдено в базе госуслуг."

    # Краткое вступление от GPT
    intro_response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Ты краткий, понятный консультан по egov"},
            {"role": "user", "content": f"Кратко объясни, что такое: {user_query}. Опиши как госуслугу, без лишних слов."}
        ],
        max_tokens=300,
        temperature=0.5
    )
    intro_text = intro_response.choices[0].message.content.strip()

    services_block = "📌 Вам могут быть полезны следующие госуслуги:\n\n"
    for r in results[:5]:
        services_block += f"🔹 <b>{r['Услуга']}</b>\n➡️ {r['Результат оказания услуги']}\n🔗 <a href='{r['Ссылка']}'>Перейти</a>\n\n"

    return f"{intro_text}\n\n{services_block}"
