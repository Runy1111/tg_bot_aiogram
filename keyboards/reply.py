from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Приветствие'),
            KeyboardButton(text='Меню'),
            KeyboardButton(text='Magica')
        ],
        [
            KeyboardButton(text='Иисус'),
            KeyboardButton(text='Аллах'),
            KeyboardButton(text='Будда')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='ДЖА ЛЕТОВ'
)

del_kb = ReplyKeyboardRemove()

start_kb2 = ReplyKeyboardBuilder()
start_kb2.add(
    KeyboardButton(text='Иисус'),
    KeyboardButton(text='Аллах'),
    KeyboardButton(text='Будда')
)
start_kb2.adjust(2, 1)


start_kb3 = ReplyKeyboardBuilder()
start_kb3.attach(start_kb2)
start_kb3.add(KeyboardButton(text='ДЖА!!!'))
start_kb3.adjust(2, 1, 1)
# start_kb3.row(KeyboardButton(text='ДЖА!!!'))  - новым рядом
