from aiogram import Router, types, F
import aiohttp
from aiogram.filters import CommandStart, Command, or_f
from dota_wr import get_info
import time
from filters.chat_types import ChatTypeFilter
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())
user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет, Питер')


@user_private_router.message(Command("menu"))
async def menu_cmd(message: types.Message):
    await message.answer("Меню:")


# @user_private_router.message(Command("wr"))
# async def check_wr(message: types.Message):
#     await message.reply("Напишите id игрока")
#
#     @user_private_router.message()
#     async def winrate(message: types.Message):
#         try:
#             await message.answer(get_info(message.text))
#         except AttributeError:
#             time.sleep(3)
#             try:
#                 await message.answer(get_info(message.text))
#             except AttributeError:
#                 time.sleep(3)
#                 try:
#                     await message.answer(get_info(message.text))
#                 except AttributeError:
#                     time.sleep(3)
#                     try:
#                         await message.answer(get_info(message.text))
#                     except AttributeError:
#                         await message.answer('try one more time')


@user_private_router.message(or_f(Command("lol"), (F.text.lower() == "ктлхувтанг")))    # или команда, или текст
@user_private_router.message(F.text, F.text.lower() == 'hello')  # '|' - или    '&' - и, оба в скобки
async def menu_cmd(message: types.Message):
    await message.answer("МАГИЯ:")


# @user_private_router.message(F.text.lower().contains('hello'))
# async def menu_cmd(message: types.Message):
#     await message.answer("МАГИЯ:2")
