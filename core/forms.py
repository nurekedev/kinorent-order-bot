from aiogram.fsm.state import StatesGroup, State


class OrderForm(StatesGroup):
    goal = State()
    phone_number = State()
    date = State()
    address = State()


class QuestionForm(StatesGroup):
    question_text = State()
