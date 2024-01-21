from aiogram.fsm.context import FSMContext
from aiogram import Router, F, Bot, html
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery, ContentType
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove
from aiogram.methods import SendMessage

import core.keyboards.buttons as keyboards

router = Router(name="Main Router")


@router.message(CommandStart())
async def show_main_menu(message: Message):
    await message.answer("Вас приветствует компания Kinorent.KZ!", reply_markup=keyboards.main_menu)


@router.message(F.text == '🍿 Арендовать проектор')
async def get_courses(message: Message):
    await message.answer("Выберите цель аренды: ", reply_markup=keyboards.goals_menu)


@router.callback_query(F.data.startswith('for_'))
async def get_rent_goal(callback: CallbackQuery):
    goal = callback.data[4:]
    await callback.message.answer(goal)
