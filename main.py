import asyncio
import os
import openai
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties

from utils.audio_converter import convert_ogg_to_wav
from speech_to_text import recognize_speech
from search_service import search_service_in_csv
from utils.config import TELEGRAM_BOT_TOKEN, TEMP_AUDIO_DIR
from gpt_logic import explain_query_with_gpt

openai.api_key = os.getenv("OPENAI_API_KEY")

bot = Bot(token=TELEGRAM_BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer("👋 Привет! Просто отправь текст или голосовое сообщение — я помогу с eGov.")

@dp.message(F.text)
async def handle_text(message: Message):
    query = message.text.strip()
    if query.startswith("/"):
        return

    results = search_service_in_csv(query)
    if results:
        gpt_reply = explain_query_with_gpt(query)
        await message.answer(f" {gpt_reply}")
    else:
        await message.answer("Ничего не найдено по вашему запросу.")

@dp.message(F.voice)
async def handle_voice(message: Message):
    voice = message.voice
    file = await bot.get_file(voice.file_id)

    os.makedirs(TEMP_AUDIO_DIR, exist_ok=True)
    ogg_path = os.path.join(TEMP_AUDIO_DIR, f"{voice.file_unique_id}.ogg")
    wav_path = os.path.join(TEMP_AUDIO_DIR, f"{voice.file_unique_id}.wav")

    await bot.download(file=file, destination=ogg_path)

    try:
        convert_ogg_to_wav(ogg_path, wav_path)

        if not os.path.exists(wav_path):
            await message.answer("❗ WAV-файл не создан. Проверь ffmpeg.")
            return

        text = recognize_speech(wav_path)
        if not text:
            await message.answer("❗ Не удалось распознать речь.")
            return

        results = search_service_in_csv(text)
        if results:
            gpt_reply = explain_query_with_gpt(text, results)
            await message.answer(f"🎙 <b>{text}</b>\n\n{gpt_reply}")
        else:
            await message.answer(f"🎙 <b>{text}</b>\n\nНичего не найдено по вашему запросу.")

    finally:
        if os.path.exists(ogg_path): os.remove(ogg_path)
        if os.path.exists(wav_path): os.remove(wav_path)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
