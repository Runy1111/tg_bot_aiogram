from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import as_list, as_marked_section, Bold

from dota_wr import get_info
import time

from keyboards import reply

from filters.chat_types import ChatTypeFilter
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())
user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет, Питер', reply_markup=reply.start_kb)


@user_private_router.message(Command("menu"))
async def menu_cmd(message: types.Message):
    await message.answer("Меню:", reply_markup=reply.start_kb2.as_markup(resize_keyboard=True,
                                                                         input_field_placeholder='Джа?'))


@user_private_router.message(F.text.lower() == 'иисус')
async def jez(message: types.Message):
    text = as_list(
        as_marked_section(
            Bold("эт кто"),
            'God',
            'son ov God',
            'Sunboy',
            marker='♥ '
        ),
        as_marked_section(
            Bold("Джа..."),
            'Летов',
            'Янка',
            'Пророк Санбой',
            marker='☺ '
        ),
        sep='\n--------------\n'
    )
    await message.reply(text.as_html())


@user_private_router.message(F.text.lower() == 'будда')
async def closer(message: types.Message):
    await message.answer('<i>Кали Юга</i>', reply_markup=reply.del_kb)


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
