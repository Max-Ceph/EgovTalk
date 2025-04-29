import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def test_gpt():
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Ты помощник."},
                {"role": "user", "content": "Что такое OpenAI?"}
            ],
            max_tokens=100
        )
        print("✅ GPT ответ:", response.choices[0].message.content)
    except Exception as e:
        print("❌ Ошибка:", e)

if __name__ == "__main__":
    test_gpt()
