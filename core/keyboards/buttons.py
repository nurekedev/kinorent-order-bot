from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from enum import Enum


class BackPath(Enum):
    TO_MAIN = 'main'
    TO_DOUBLE_REMOVE = 'd_main'
    TO_LANGUAGES = 'goals'


goals_builder = InlineKeyboardBuilder()

main_menu_buttons = [
    [KeyboardButton(text='🍿 Арендовать проектор')],
    [KeyboardButton(text='☎️ Заказать звонок')],
    [KeyboardButton(text='🛠 Инструкция сборки'),
     KeyboardButton(text='🪩 Мы в Instagram')]
]

main_menu = ReplyKeyboardMarkup(keyboard=main_menu_buttons,
                                resize_keyboard=True,
                                input_field_placeholder='Выберите пункт ниже 👇🏽')

goals = [
    "Рисование настенных рисунков",
    "Для киновечера",
    "Презентация",
    "В других целях"
]




goals_kb_buttons = [
    [InlineKeyboardButton(text=f"{goal}", callback_data=f'for_{goal}')] for goal in goals
]
goals_kb_buttons.append([InlineKeyboardButton(text='Назад', callback_data=f"back_to_{BackPath.TO_MAIN.value}")])

goals_menu = InlineKeyboardMarkup(inline_keyboard=goals_kb_buttons)
