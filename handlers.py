from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("POST"), KeyboardButton("PROGNOZ"))
keyboard.add(KeyboardButton("POISK"), KeyboardButton("POMOSH"))

async def cmd_start(message: types.Message):
    await message.answer("👋 Привет! Я бот 'Дети Света' ☀️", reply_markup=keyboard)

async def cmd_post(message: types.Message):
    await message.answer("✨ Здесь будет генерация поста в стиле Солнышка.")

async def cmd_prognoz(message: types.Message):
    await message.answer("🔮 Энергопрогноз на день: уравновешенность, мягкость, принятие.")

async def cmd_poisk(message: types.Message):
    await message.answer("🔍 Напиши ключевое слово — я поищу в архиве (в разработке).")

async def cmd_pomosh(message: types.Message):
    await message.answer("📖 Команды:
/start — запуск
/post — пост в стиле Солнышка
/prognoz — энергопрогноз
/poisk — поиск по архиву
/pomosh — помощь")

async def btn_handler(message: types.Message):
    text = message.text.lower()
    if text == "post":
        await cmd_post(message)
    elif text == "prognoz":
        await cmd_prognoz(message)
    elif text == "poisk":
        await cmd_poisk(message)
    elif text == "pomosh":
        await cmd_pomosh(message)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])
    dp.register_message_handler(cmd_post, commands=["post"])
    dp.register_message_handler(cmd_prognoz, commands=["prognoz"])
    dp.register_message_handler(cmd_poisk, commands=["poisk"])
    dp.register_message_handler(cmd_pomosh, commands=["pomosh"])
    dp.register_message_handler(btn_handler, lambda message: message.text in ["POST", "PROGNOZ", "POISK", "POMOSH"])