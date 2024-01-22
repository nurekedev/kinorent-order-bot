from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from enum import Enum


class BackPath(Enum):
    TO_MAIN = 'main'
    TO_DOUBLE_REMOVE = 'd_main'
    TO_PACKAGES = 'packages'


main_menu_buttons = [
    [KeyboardButton(text='🍿 Арендовать проектор')],
    [KeyboardButton(text='☎️ Заказать звонок')],
    [KeyboardButton(text='🛠 Инструкция сборки'),
     KeyboardButton(text='🪩 Мы в Instagram')]
]

main_menu = ReplyKeyboardMarkup(keyboard=main_menu_buttons,
                                resize_keyboard=True,
                                input_field_placeholder='Выберите пункт ниже 👇🏽')

package_menu_buttons = [
    [InlineKeyboardButton(text="Базовый набор (6 000₸)", callback_data=f'package_basic')],
    [InlineKeyboardButton(text="Базовый + Экран за (9 000₸)", callback_data=f'package_medium')],
    [InlineKeyboardButton(text="Полный пакет (12 000₸)", callback_data=f'package_vip')],
    [InlineKeyboardButton(text='Назад', callback_data=f"back_to_{BackPath.TO_MAIN.value}")]
]

package_menu = InlineKeyboardMarkup(inline_keyboard=package_menu_buttons)

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

action_menu_buttons = [
    [InlineKeyboardButton(text='Назад', callback_data=f"back_to_{BackPath.TO_MAIN.TO_PACKAGES}"),
     InlineKeyboardButton(text="Оформить заказ", callback_data="perform_order")]
]

action_menu = InlineKeyboardMarkup(inline_keyboard=action_menu_buttons)


