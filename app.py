import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dota_wr import get_info


bot = Bot(token="8156406562:AAHO2MCc5i9ZFhvdlJGwcGsqFMhHLvkNR6s")
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет, Питер')


@dp.message()
async def echo(message: types.Message):
    if message.text[:3] == '/wr':
        await message.answer(get_info(message.text[3:]))
    else:
        await message.answer(message.text)


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
