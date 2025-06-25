import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart


bot = Bot(token="8156406562:AAHO2MCc5i9ZFhvdlJGwcGsqFMhHLvkNR6s")
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет, Питер')


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
