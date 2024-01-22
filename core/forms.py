from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

"""
Для формирования заказа нам нужны:
1. Username TG
2. Цель аренды
3. Выбранный пакет
4. Вид доставки
5. Дата
6. Адрес
"""


class OrderForm(StatesGroup):
    packet = State()
    name = State()
    goal = State()
    username = State()
    delivery = State()
    date = State()
    address = State()
