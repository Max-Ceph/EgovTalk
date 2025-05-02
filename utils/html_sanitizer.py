import re

ALLOWED_TAGS = ['b', 'i', 'u', 's', 'code', 'pre', 'a', 'br']

def clean_telegram_html(text: str) -> str:
    text = re.sub(r'(?i)<!DOCTYPE.*?>', '', text)
    text = re.sub(r'(?i)</?(html|head|body|h\d|meta|style|script|ul|li|strong|em)[^>]*>', '', text)

    text = re.sub(
        rf'</?(?!({"|".join(ALLOWED_TAGS)}))\w+[^>]*>',
        '',
        text
    )

    return text.strip()
