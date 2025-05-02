import os
from openai import OpenAI
from dotenv import load_dotenv
from search_service import search_service_in_csv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def explain_query_with_gpt(user_query: str, results: list[dict]) -> str:


    if results:
        intro_response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Ты государственный консультант. Отвечай строго, чётко, кратко (1-2 предложения), без повторений. "
                        "Не повторяй вопрос пользователя. Избегай воды. Используй только официальные формулировки, если можешь. "
                        "Никогда не пиши слово более одного раза. Формат ответа — HTML. "
                    )
                },

                {"role": "user",
                 "content": f"Кратко объясни, что такое: {user_query}. Опиши как госуслугу, без лишних слов."}
            ],
            max_tokens=300,
            temperature=0.5
        )
        intro_text = intro_response.choices[0].message.content.strip()

        services_block = "📌 Вам могут быть полезны следующие госуслуги:\n\n"
        for r in results[:5]:
            services_block += (
                f"🔹 <b>{r['Услуга']}</b>\n"
                f"➡️ {r['Результат оказания услуги']}\n"
                f"🔗 <a href='{r['Ссылка']}'>Перейти</a>\n\n"
            )

        return f"{intro_text}\n\n{services_block}"

    else:
        fallback_response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system",
                 "content": "Ты краткий, понятный консультант по egov, разбирающийся в казахстанских законах. Отвечай в HTML-формате, не используй Markdown."},
                {"role": "user",
                 "content": f"Пользователь задал вопрос: {user_query}. Объясни, какая может быть полезна информация или услуга, если даже точных совпадений в базе нет."}
            ],
            max_tokens=300,
            temperature=0.5
        )
        return fallback_response.choices[0].message.content.strip()
