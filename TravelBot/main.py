import logging
import config
import aiohttp
import states

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from TravelBot.keybords import city_choice

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    Welcome message, I'll rewrite this later
    """
    await message.reply("Hi!\nTest message")


@dp.message_handler(commands='weather')
async def weather_options(message: types.Message):
    """
    Get keyword with options from what city we want to learn information
    about weather
    """
    await message.reply("Choose a city", reply_markup=city_choice)


@dp.callback_query_handler(text_startswith='city')
async def weather_preset_option(call: types.CallbackQuery):
    """
    Chose a one of preset cities to receive information about weather there
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(config.WEATHER_API.format(call.data.split("_")[1])) as response:
            var = await response.json()
            await call.message.edit_text(text=f'City: {var["name"]}\n'
                                              f'Temperature: {var["main"]["temp"]}°C\n'
                                              f'Feels like: {var["main"]["feels_like"]}°C\n'
                                              f'Humidity: {var["main"]["humidity"]}%\n'
                                              f'Pressure: {var["main"]["pressure"]}\n'
                                              f'Wind: {var["wind"]["speed"]}\n'
                                              f'Description: {var["weather"][0]["description"]}')


@dp.callback_query_handler(text_contains='other')
async def weather_other_option(call: types.CallbackQuery):
    """
    If a user has selected an 'Other' option, this handler sets a state for another handler,
    that allows input custom name of a city
    """
    await states.City.city.set()
    await call.message.edit_text(text="Enter a city name")


@dp.message_handler(state=states.City.city)
async def input_city(message: types.Message, state: FSMContext):
    """
    Get information about weather of a custom city
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(config.WEATHER_API.format(message.text)) as response:
            var = await response.json()
            await message.answer(text=f'City: {var["name"]}\n'
                                      f'Temperature: {var["main"]["temp"]}°C\n'
                                      f'Feels like: {var["main"]["feels_like"]}°C\n'
                                      f'Humidity: {var["main"]["humidity"]}%\n'
                                      f'Pressure: {var["main"]["pressure"]}\n'
                                      f'Wind: {var["wind"]["speed"]}\n'
                                      f'Description: {var["weather"][0]["description"]}')
            await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)