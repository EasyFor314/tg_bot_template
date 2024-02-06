from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard=[
    InlineKeyboardButton(text='Тестовая кнопка', callback_data="test_callback"),
]
start_button = InlineKeyboardMarkup(row_width=1)
start_button.add(*keyboard)