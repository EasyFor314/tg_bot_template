import logging
import uuid
from aiogram import types
from handlers.inline_keyboard import start_button

async def bot_start(msg: types.Message):
    try:
        await msg.answer(f'Привет, я шаблон тестового бота', reply_markup=start_button )
    except Exception as exception:
        logging.error(f'Exception : {exception}')

async def test_message_handler(msg: types.Message):
    try:
        output_msg = 'Я получил текст: ' + str(msg.text)
        await msg.answer(output_msg, parse_mode= "Markdown")
    except Exception as error:
        logging.error('Возникла ошибка {0}'.format(str(error)))
        await msg.answer("Произошла ошибка, повторите позднее")

async def test_callback(call: types.CallbackQuery):
    try:
        output_msg = 'Я тестовый callback'
        await call.message.answer(output_msg, parse_mode= "Markdown") 
        await call.answer()
    except Exception as error:
        logging.error('Возникла ошибка {0}'.format(str(error)))
        await call.message.answer('Произошла ошибка, повторите позднее', parse_mode= "Markdown")