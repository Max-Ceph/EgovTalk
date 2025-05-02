import asyncio
import os
import logging
import openai

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton
from aiogram.client.default import DefaultBotProperties

from keyboard_menu import menu_keyboard
from utils.audio_converter import convert_ogg_to_wav
from speech_to_text import recognize_speech
from search_service import search_service_in_csv
from utils.config import TELEGRAM_BOT_TOKEN, TEMP_AUDIO_DIR
from gpt_logic import explain_query_with_gpt
from utils.html_sanitizer import clean_telegram_html
from menu_router import router as menu_router



logging.basicConfig(level=logging.INFO)
openai.api_key = os.getenv("OPENAI_API_KEY")

bot = Bot(token=TELEGRAM_BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()
dp.include_router(menu_router)


start_buttons = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="📂 Меню услуг")]],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(
        "👋 Добро пожаловать! Я помогу найти нужную госуслугу.\n\n"
        "Вы можете ввести запрос вручную или воспользоваться меню.",
        reply_markup=start_buttons
    )

@dp.message(F.text == "📂 Меню услуг")
async def show_menu(message: Message):
    await message.answer("📂 Выберите категорию:", reply_markup=menu_keyboard)



@dp.message(F.text)
async def handle_text(message: Message):
    query = message.text.strip()
    if query.startswith("/"):
        return
    results = search_service_in_csv(query)
    gpt_reply = explain_query_with_gpt(query, results)
    await message.answer(clean_telegram_html(gpt_reply))

@dp.message(F.voice)
async def handle_voice(message: Message):
    voice = message.voice
    file = await bot.get_file(voice.file_id)

    os.makedirs(TEMP_AUDIO_DIR, exist_ok=True)
    ogg_path = os.path.join(TEMP_AUDIO_DIR, f"{voice.file_unique_id}.ogg")
    wav_path = os.path.join(TEMP_AUDIO_DIR, f"{voice.file_unique_id}.wav")

    await bot.download(file, destination=ogg_path)


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
        gpt_reply = explain_query_with_gpt(text, results)
        await message.answer(f"🎙 <b>{text}</b>\n\n{clean_telegram_html(gpt_reply)}")
    finally:
        for path in (ogg_path, wav_path):
            if os.path.exists(path):
                os.remove(path)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
