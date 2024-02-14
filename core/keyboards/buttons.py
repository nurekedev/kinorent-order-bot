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
    SHOW_MENU = 'main_menu'


main_menu_buttons = [
    [KeyboardButton(text='🍿 Арендовать проектор')],
    [KeyboardButton(text='☎️ Заказать звонок')],
    [KeyboardButton(text='🛠 Инструкция сборки'),
     KeyboardButton(text='🪩 Cоциальные сети')]
]

main_menu = ReplyKeyboardMarkup(keyboard=main_menu_buttons,
                                resize_keyboard=True,
                                input_field_placeholder='Выберите пункт ниже 👇🏽')

package_menu_buttons = [
    [InlineKeyboardButton(text="🎨 Базовый набор (6 000₸)", callback_data=f'package_basic')],
    [InlineKeyboardButton(text="🎬 Базовый + Экран за (9 000₸)", callback_data=f'package_medium')],
    [InlineKeyboardButton(text="🌟 Полный пакет (12 000₸)", callback_data=f'package_vip')],
    [InlineKeyboardButton(text="🚘 Кинотеатр в машине (6 000₸)", callback_data=f'package_car')],
    [InlineKeyboardButton(text='🔙 Назад', callback_data=f"back_to_{BackPath.TO_MAIN.value}")]
]

package_menu = InlineKeyboardMarkup(inline_keyboard=package_menu_buttons)

goals = [
    "🎨 Рисование настенных рисунков",
    "🎬 Для киновечера",
    "📊 Презентация",
    "🎉 Мероприятие",
    "📝 В других целях"
    "🚘 Просмотра в автомобиле"
]

goals_kb_buttons = [
    [KeyboardButton(text=f"{goal}")] for goal in goals
]

goals_menu = ReplyKeyboardMarkup(keyboard=goals_kb_buttons,
                                 resize_keyboard=True,
                                 input_field_placeholder='В каких целях вы планируете арендовать 👇🏽')

action_menu_buttons = [
    [InlineKeyboardButton(text='🔙 Назад', callback_data=f"back_to_{BackPath.TO_MAIN.TO_PACKAGES}"),
     InlineKeyboardButton(text="🛒 Оформить заказ", callback_data="perform_order")]
]

action_menu = InlineKeyboardMarkup(inline_keyboard=action_menu_buttons)

contact_kb_buttons = [
    [KeyboardButton(text="Отправить контакт 👤", request_contact=True)]
]

contact_menu = ReplyKeyboardMarkup(keyboard=contact_kb_buttons, resize_keyboard=True)

request_call = [
    [KeyboardButton(text="🔙 Назад"),
     KeyboardButton(text="Отправить номер 👤", request_contact=True)]
]
request_call_menu = ReplyKeyboardMarkup(keyboard=request_call, resize_keyboard=True)


social_media_buttons = [
    [InlineKeyboardButton(text='📷 Instagram', url='https://www.instagram.com/kinorent.kz/'),
     InlineKeyboardButton(text="🎵 TikTok", url='https://www.tiktok.com/@kinorentkz?_t=8jPHfLXU76r&_r=1')],
    [InlineKeyboardButton(text='🔙 Назад', callback_data="back_to_main")]
]

social_menu = InlineKeyboardMarkup(inline_keyboard=social_media_buttons)

instruction_list = [
    [InlineKeyboardButton(text='📽️ Проектор Wanbo T2/Max/R', url='https://youtu.be/w1AnVElgmA4')],
    [InlineKeyboardButton(text='📽️ Проектор Wanbo T6/Max', url='https://youtu.be/Od-mlRG_G5M')],
    [InlineKeyboardButton(text='🔧 Сборка штатива', callback_data='guide_instruction')],
    [InlineKeyboardButton(text='🔙 Назад', callback_data='back_to_')]
]

instruction_menu = InlineKeyboardMarkup(inline_keyboard=instruction_list)
