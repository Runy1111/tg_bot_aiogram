import asyncio
import datetime
import time

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dota_wr import get_info


bot = Bot(token="8156406562:AAHO2MCc5i9ZFhvdlJGwcGsqFMhHLvkNR6s")    #KEEP YOUR DAMN HANDS OFF MY TOKEN!
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет, Питер')


@dp.message()
async def echo(message: types.Message, bot: Bot):
    # await bot.send_message(message.from_user.ip, 'QWE')
    if message.text[:3] == '/wr':
        try:
            await message.answer(get_info(message.text[3:]))
        except AttributeError:
            await message.answer('try one more time')
    else:
        await message.answer(message.text)


async def main():
    print(datetime.datetime.now(), "Bot started!")
    await dp.start_polling(bot)


asyncio.run(main())
