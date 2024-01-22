from aiogram.fsm.context import FSMContext
from aiogram import Router, F, Bot, html
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery, ContentType
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import (ReplyKeyboardRemove, FSInputFile, InputFile, ReplyKeyboardMarkup, KeyboardButton)
from aiogram.methods import SendMessage

import core.keyboards.buttons as keyboards
import core.forms as forms
import core.handlers.handle_data as handle_data

import os

router = Router(name="Main Router")
path = "/Users"


@router.message(CommandStart())
async def show_main_menu(message: Message):
    await message.answer("Вас приветствует компания Kinorent.KZ!", reply_markup=keyboards.main_menu)


@router.message(F.text == '🍿 Арендовать проектор')
async def get_courses(message: Message):
    await message.answer("Выберите цель аренды: ", reply_markup=keyboards.package_menu)


@router.callback_query(F.data.startswith('package_'))
async def get_packages(callback: CallbackQuery):
    global package_to_compare
    package_to_compare = callback.data[8:]
    print(package_to_compare)

    photo_path = FSInputFile(
        os.path.join(path, "nurzhansaktaganov/Desktop/kinorent/kinorent-bot/assets", f"{package_to_compare}.jpeg"))
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
async def perform_order(callback: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(forms.OrderForm.name)
    await callback.message.answer("Отлично! Как вам обращаться? \nКеремет! Сізді қалай атасам болады?",
                                  reply_markup=ReplyKeyboardRemove())


# @router.message(forms.OrderForm.name)
# async def process_name(message: Message, state: FSMContext) -> None:
#     await state.update_data(name=message.text)
#     await state.set_state(forms.OrderForm.goal)
#     await message.answer(
#         f"Nice to meet you, {html.quote(message.text)}!\nDid you like to write bots?",
#         reply_markup=ReplyKeyboardMarkup(
#             keyboard=[
#                 [
#                     KeyboardButton(text="Yes"),
#                     KeyboardButton(text="No"),
#                 ]
#             ],
#             resize_keyboard=True,
#         ),
#     )
