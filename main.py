from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import logging
import os

API_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

# Клавиатура
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("POST"), KeyboardButton("PROGNOZ"))
keyboard.add(KeyboardButton("POISK"), KeyboardButton("POMOSH"))

@dp.message_handler(commands=['start'])
async def cmd_start(message: Message):
    await message.answer("Привет! Я бот 'Дети Света' ☀️", reply_markup=keyboard)

@dp.message_handler(commands=['post'])
async def cmd_post(message: Message):
    await message.answer("✨ Здесь будет генерация поста в стиле Солнышка.")

@dp.message_handler(commands=['prognoz'])
async def cmd_prognoz(message: Message):
    await message.answer("🌞 Энергопрогноз на день: спокойствие, принятие, любовь.")

@dp.message_handler(commands=['pomosh'])
async def cmd_pomosh(message: Message):
    await message.answer("🔍 Доступные команды:
/post — создать пост
/prognoz — получить энергопрогноз
/poisk — найти по архиву
/pomosh — помощь")

@dp.message_handler(commands=['poisk'])
async def cmd_poisk(message: Message):
    await message.answer("🔎 Введите ключевое слово для поиска по архиву (в разработке).")

@dp.message_handler(lambda message: message.text in ["POST", "PROGNOZ", "POISK", "POMOSH"])
async def handle_buttons(message: Message):
    command = message.text.lower()
    await message.answer(f"Выполняю команду /{command}...")
    await bot.send_message(chat_id=message.chat.id, text=f"✨ Здесь будет ответ для /{command} (временно шаблонный).")

if __name__ == '__main__':
    executor.start_polling(dp)
