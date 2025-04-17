from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Кнопки
menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
menu_kb.add(KeyboardButton("📝 POST — сгенерировать пост"))
menu_kb.add(KeyboardButton("🔮 PROGNOZ — получить прогноз"))
menu_kb.add(KeyboardButton("🔍 POISK — найти пост по теме"))
menu_kb.add(KeyboardButton("🆘 POMOSH — помощь и инструкция"))


# Команда /start
async def start_handler(message: types.Message):
    text = (
        "👋 Привет! Я бот *Дети Света*. Готов помогать тебе создавать посты и прогнозы ✨\n\n"
        "📋 *Доступные команды:*\n"
        "📝 POST — сгенерировать пост\n"
        "🔮 PROGNOZ — получить прогноз\n"
        "🔍 POISK — найти пост по теме\n"
        "🆘 POMOSH — помощь и инструкция"
    )
    await message.answer(text, parse_mode="Markdown", reply_markup=menu_kb)


# Ответы на кнопки
async def handle_post(message: types.Message):
    await message.answer("✍️ Генерирую пост... (пока заглушка)")


async def handle_prognoz(message: types.Message):
    await message.answer("🔮 Генерирую прогноз... (пока заглушка)")


async def handle_poisk(message: types.Message):
    await message.answer("🔍 Поиск по теме... (пока заглушка)")


async def handle_pomosh(message: types.Message):
    await message.answer("🆘 Инструкция и помощь... (пока заглушка)")


# Регистрация хендлеров
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=["start"])
    dp.register_message_handler(handle_post, lambda m: "POST" in m.text)
    dp.register_message_handler(handle_prognoz, lambda m: "PROGNOZ" in m.text)
    dp.register_message_handler(handle_poisk, lambda m: "POISK" in m.text)
    dp.register_message_handler(handle_pomosh, lambda m: "POMOSH" in m.text)
