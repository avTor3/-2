import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

API_TOKEN = os.getenv("API_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID", "-1001234567890"))

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(commands=["start"])
async def start_cmd(message: types.Message):
    await message.answer(
        "Привет! Я бот книжного клуба 📚\n"
        "Команды:\n"
        "/recommend - получить рекомендацию\n"
        "/schedule - узнать расписание\n"
        "/vote - проголосовать"
    )

@dp.message(commands=["recommend"])
async def recommend(message: types.Message):
    await message.answer("Рекомендую прочитать «1984» Дж. Оруэлла 📖")

@dp.message(commands=["schedule"])
async def schedule(message: types.Message):
    await message.answer("📅 Следующая встреча: 15 сентября 2025, 19:00")

@dp.message(commands=["vote"])
async def vote(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="1984", callback_data="vote_1984")],
        [InlineKeyboardButton(text="451° по Фаренгейту", callback_data="vote_451")],
        [InlineKeyboardButton(text="Война и мир", callback_data="vote_war")],
    ])
    await message.answer("Голосуем за следующую книгу:", reply_markup=keyboard)

@dp.callback_query()
async def handle_vote(callback: types.CallbackQuery):
    choice = callback.data.replace("vote_", "")
    await callback.message.answer(f"Спасибо! Вы выбрали: {choice}")
    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
