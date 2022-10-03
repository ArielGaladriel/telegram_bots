from aiogram import types
from loader import dp


@dp.message_handler(commands='start')
async def start_menu(message: types.Message):
    """
    This is a  test function
    """
    await message.reply("Test")


@dp.message_handler()
async def start_menu(message: types.Message):
    """
    This is an echo function
    """
    await message.reply(f'Income: {message.text}')
