from aiogram import types
from aiogram.dispatcher import Dispatcher

def register_handlers(dp: Dispatcher):
    @dp.message_handler(commands=["start"])
    async def start_command(message: types.Message):
        await message.answer(
            "👋 Привет! Я бот 'Дети Света'. Готов помогать тебе создавать посты и прогнозы ✨"
        )
        await message.answer(
            "📋 Доступные команды:\n\n"
            "📮 POST — сгенерировать пост\n"
            "🔮 PROGNOZ — получить прогноз\n"
            "🔍 POISK — найти пост по теме\n"
            "🆘 POMOSH — помощь и инструкция"
        )

    @dp.message_handler(commands=["post"])
    async def post_command(message: types.Message):
        await message.answer("✍️ Генерирую пост... (пока заглушка)")

    @dp.message_handler(commands=["prognoz"])
    async def prognoz_command(message: types.Message):
        await message.answer("🔮 Генерирую прогноз... (пока заглушка)")

    @dp.message_handler(commands=["poisk"])
    async def poisk_command(message: types.Message):
        await message.answer("🔍 Поиск по архиву... (пока заглушка)")

    @dp.message_handler(commands=["pomosh"])
    async def pomosh_command(message: types.Message):
        await message.answer(
            "🆘 Помощь:\n"
            "Напиши /post чтобы создать пост\n"
            "Напиши /prognoz чтобы получить прогноз\n"
            "Напиши /poisk чтобы найти пост\n"
            "Всё просто 😊"
        )
