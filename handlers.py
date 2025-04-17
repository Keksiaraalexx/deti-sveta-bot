from aiogram import types, Dispatcher

async def cmd_start(message: types.Message):
    await message.answer("👋 Привет! Я бот 'Дети Света'. Готов к работе!")

async def cmd_post(message: types.Message):
    await message.answer("✨ Здесь будет генерация поста в стиле Солнышка.")

async def cmd_prognoz(message: types.Message):
    await message.answer("🔮 Энергопрогноз на день будет готов через мгновение...")

async def cmd_poisk(message: types.Message):
    await message.answer("🔍 Напиши тему, и я найду нужный пост в архиве.")

async def cmd_pomosh(message: types.Message):
    await message.answer("📖 Доступные команды:
/start
/post
/prognoz
/poisk
/pomosh")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])
    dp.register_message_handler(cmd_post, commands=["post"])
    dp.register_message_handler(cmd_prognoz, commands=["prognoz"])
    dp.register_message_handler(cmd_poisk, commands=["poisk"])
    dp.register_message_handler(cmd_pomosh, commands=["pomosh"])