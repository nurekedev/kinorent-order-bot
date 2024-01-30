from aiogram.fsm.context import FSMContext
from aiogram import Router, F, Bot
from aiogram.filters import Command, CommandStart, StateFilter, Filter
from aiogram.types import Message, CallbackQuery
from aiogram.types import ReplyKeyboardRemove, FSInputFile
from typing import Any, Dict
from functools import lru_cache

import core.keyboards.buttons as keyboards
import core.forms as forms
import core.handlers.handle_data as handle_data

import os
import re
import config
import uuid

router = Router(name="Main Router")
package_to_compare = "не выбран"


@lru_cache(maxsize=100)
def send_photo_with_caption_and_markup(path, project_path, file_extension, filename):
    return FSInputFile(os.path.join(path, project_path, f"{filename}.{file_extension}"))


@router.message(CommandStart())
async def show_main_menu(message: Message):
    await message.answer("Вас приветствует компания Kinorent.KZ!", reply_markup=keyboards.main_menu)


@router.message(F.text == '🍿 Арендовать проектор')
async def get_courses(message: Message):
    photo_path = send_photo_with_caption_and_markup(config.settings['USER_PATH'], config.settings['PROJECT_PATH'],
                                                    "jpg", "hello")

    await message.answer_photo(photo=photo_path, reply_markup=keyboards.package_menu)


@router.message(F.text == '☎️ Заказать звонок')
async def share_phone_number(message: Message):
    await message.answer("🇰🇿 Нажмите на кнопку ниже для заказа звонка"
                         "\n🇷🇺 Қоңырау тапсырыс беру үшін батырманы бас", reply_markup=keyboards.request_call_menu)


@router.message(F.text == '🪩 Cоциальные сети')
async def social_media(message: Message):
    await message.answer("Наши соцальные сети:", reply_markup=keyboards.social_menu)


@router.message(F.text == '🛠 Инструкция сборки')
async def get_instruction(message: Message):
    await message.answer("Список инструкции:", reply_markup=keyboards.instruction_menu)


@router.message(F.text == '🔙 Назад')
async def back_to_main(message: Message):
    await message.answer("Вас приветствует компания Kinorent.KZ!", reply_markup=keyboards.main_menu)


@router.callback_query(F.data.startswith('package_'))
async def get_packages(callback: CallbackQuery):
    global package_to_compare
    package_to_compare = callback.data[8:]

    photo_path = send_photo_with_caption_and_markup(config.settings['USER_PATH'], config.settings['PROJECT_PATH'],
                                                    "jpeg",
                                                    package_to_compare)

    await callback.message.answer_photo(photo=photo_path, caption=handle_data.package_data[f'{package_to_compare}'],
                                        reply_markup=keyboards.action_menu)


@router.callback_query(F.data.startswith('back_to_'))
async def back_to_main(callback: CallbackQuery):
    removing = callback.data[8:]
    await callback.bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)

    if removing == 'd_main':
        await callback.bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id - 1)
    elif removing == 'main':
        await callback.answer(reply_markup=keyboards.main_menu)
    elif removing == 'packages':
        await callback.answer(reply_markup=keyboards.package_menu)


@router.callback_query(F.data.startswith('perform_order'))
async def perform_goal(callback: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(forms.OrderForm.goal)
    await callback.message.answer(
        f"В каких целях вы хотите арендовать?", reply_markup=keyboards.goals_menu
    )


@router.message(forms.OrderForm.goal)
async def process_date(message: Message, state: FSMContext) -> None:
    await state.update_data(goal=message.text)
    await state.set_state(forms.OrderForm.date)
    await message.answer(
        "🇰🇿 Қай күнге және қай уақытқа жоспарлап отырсыз? \n🇷🇺 На какую дату и время планируете? \n\n<b>Пример:</b> \n<i>- 05.02 17:00</i> \n<i>- Сегодня в 12:00</i>",
        reply_markup=ReplyKeyboardRemove())


@router.message(forms.OrderForm.date)
async def process_address(message: Message, state: FSMContext) -> None:
    await state.update_data(date=message.text)
    await state.set_state(forms.OrderForm.address)
    await message.answer(
        "🇰🇿 Мекен жайыңызды енгізіңіз \n🇷🇺 Напишите адрес \n\n<b>Пример:</b> \n<i>- ул Манаса X, X подъезд, X кв</i> \n<i>- БЦ Атакент, X этаж, X бутик</i>",
        reply_markup=ReplyKeyboardRemove())


@router.message(forms.OrderForm.address)
async def process_phone_number(message: Message, state: FSMContext) -> None:
    await state.update_data(address=message.text)
    await state.set_state(forms.OrderForm.phone_number)
    await message.answer(
        "🇰🇿 Жіберу үшін <b>Отправить номер 👤</b> басыңыз\n"
        "🇷🇺 Для отправки данных, нажмите на кнопку <b>Отправить номер 👤</b>",
        reply_markup=keyboards.contact_menu)


@router.message(F.contact, forms.OrderForm.phone_number)
async def process_get_data(message: Message, state: FSMContext) -> None:
    await state.update_data(phone_number=message.contact.phone_number)
    data = await state.get_data()
    await show_summary(message=message, data=data)
    await state.clear()


async def show_summary(message: Message, data: Dict[str, Any]) -> None:
    goal = data.get('goal', '')
    phone_number = data.get('phone_number', '')
    date = data.get('date', '')
    address = data.get('address', '')

    data_to_hash = f"{message.from_user.full_name}{message.from_user.username}{package_to_compare}{goal}{phone_number}{date}{address}"
    order_uuid_hash = uuid.uuid5(uuid.NAMESPACE_DNS, data_to_hash)

    summary_text = (f"🆔 {order_uuid_hash}"
                    f"\nИмя клиента: {message.from_user.full_name}"
                    f"\nusername: @{message.from_user.username}"
                    f"\nВыбранный набор: {package_to_compare}"
                    f"\nЦель аренды: {goal}"
                    f"\nНомер телефона: {phone_number}"
                    f"\nДата: {date}"
                    f"\nАдрес: {address}")

    photo_path = send_photo_with_caption_and_markup(config.settings['USER_PATH'], config.settings['PROJECT_PATH'],
                                                    "jpg", "map")

    await message.bot.send_photo(
        chat_id=message.chat.id,
        photo=photo_path,
        caption=(
            f"Отлично, {message.from_user.full_name}! 🌟\n"
            "👩🏼‍💻 Статус: Передан к менеджерам\n"

            "\nСейчас можете ознакомиться с нашей картой бесплатной доставки 🗺️"
        ),
        reply_markup=keyboards.main_menu
    )

    await message.bot.send_message(chat_id=config.settings['TELEGRAM_MANAGERS'], text=summary_text)


@router.callback_query(F.data.startswith('guide_'))
async def get_guide_photo(callback: CallbackQuery):
    guide_number = callback.data[6:]
    photo_path = send_photo_with_caption_and_markup(config.settings['USER_PATH'], config.settings['PROJECT_PATH'],
                                                    "png", guide_number)
    await callback.message.answer_photo(photo=photo_path, reply_markup=keyboards.main_menu)


@router.message(F.contact)
async def send_phone_number(message: Message) -> None:
    await message.bot.send_message(chat_id=config.settings['TELEGRAM_MANAGERS'], text='‼️Необходимо связаться:')
    await message.bot.forward_message(chat_id=config.settings['TELEGRAM_MANAGERS'], from_chat_id=message.chat.id,
                                      message_id=message.message_id)
    await message.answer(
        text=(
            f"Спасибо, {message.from_user.full_name}! 🌟\n"
            "В ближайшее время на указанный вами номер будет совершен звонок. ☎️\n"
            f"Номер: {message.contact.phone_number}"
        ),
        reply_markup=keyboards.main_menu
    )


@router.message()
async def no_idea(message: Message):
    await message.answer("Я вас не понимаю 🤷‍♂️")
