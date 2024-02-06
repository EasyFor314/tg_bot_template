from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart, CommandHelp, Command

from .base_handlers import bot_start, test_message_handler, test_callback

def setup(dp: Dispatcher):
    dp.register_message_handler(bot_start, CommandStart())
    dp.register_message_handler(test_callback)
    dp.register_callback_query_handler(test_callback, lambda callback_query: callback_query.data == "test_callback" )