import logging
import config
import aiohttp
import states

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from keybords import city_choice, currency_choice, transliteration
from functions import armenian_transliteration_eastern, armenian_transliteration_western, georgian_transliteration

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
    Get a keyboard with options from what city we want to learn information
    about weather
    """
    await message.reply("Choose a city", reply_markup=city_choice)


@dp.callback_query_handler(text_startswith='city')
async def weather_preset_option(call: types.CallbackQuery):
    """
    Choose a one of preset cities to receive information about weather there
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(config.WEATHER_API.format(call.data.split("_")[1])) as response:
            weather = await response.json()
            await call.message.edit_text(text=f'City: {weather["name"]}\n'
                                              f'Temperature: {weather["main"]["temp"]}°C\n'
                                              f'Feels like: {weather["main"]["feels_like"]}°C\n'
                                              f'Humidity: {weather["main"]["humidity"]}%\n'
                                              f'Pressure: {weather["main"]["pressure"]}\n'
                                              f'Wind: {weather["wind"]["speed"]}\n'
                                              f'Description: {weather["weather"][0]["description"]}')


@dp.callback_query_handler(text_contains='other_weather')
async def weather_other_option(call: types.CallbackQuery):
    """
    If a user has selected an 'Other' option, this handler sets a state for another handler,
    that allows input custom name of a city
    """
    await states.City.city.set()
    await call.message.edit_text(text="Enter a city name like: \'paris\'")


@dp.message_handler(state=states.City.city)
async def input_city(message: types.Message, state: FSMContext):
    """
    Get information about weather of a custom city
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(config.WEATHER_API.format(message.text)) as response:
            weather = await response.json()
            await message.answer(text=f'City: {weather["name"]}\n'
                                      f'Temperature: {weather["main"]["temp"]}°C\n'
                                      f'Feels like: {weather["main"]["feels_like"]}°C\n'
                                      f'Humidity: {weather["main"]["humidity"]}%\n'
                                      f'Pressure: {weather["main"]["pressure"]}\n'
                                      f'Wind: {weather["wind"]["speed"]}\n'
                                      f'Description: {weather["weather"][0]["description"]}')
            await state.finish()


@dp.message_handler(commands='exchange')
async def weather_options(message: types.Message):
    """
    Get a keyboard with options what exchange rates you want to know
    """
    await message.reply("Choose currencies", reply_markup=currency_choice)


@dp.callback_query_handler(text_startswith='currency')
async def currency_preset_option(call: types.CallbackQuery):
    """
    Choose a one of preset currency pairs to receive information about exchange rates
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(config.CURRENCY_API.format(call.data.split("_")[1], call.data.split("_")[2])) as response:
            rates = await response.json()
            await call.message.edit_text(text=f'From: {rates["base_currency_name"]}\n'
                                              f'To: {list(rates["rates"].values())[0]["currency_name"]}\n'
                                              f'Rate: {list(rates["rates"].values())[0]["rate"]}')


@dp.callback_query_handler(text_contains='other_currency')
async def weather_other_option(call: types.CallbackQuery):
    """
    If a user has selected an 'Other' option, this handler sets a state for another handler,
    that allows input custom currency pair
    """
    await states.Country.country.set()
    await call.message.edit_text(text="Enter a currency pair with whitespace like: \'usd eur\'")


@dp.message_handler(state=states.Country.country)
async def input_city(message: types.Message, state: FSMContext):
    """
    Get information about exchange rate between a custom currency pair
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(config.CURRENCY_API.format(message.text.split(' ')[0],message.text.split(' ')[1])) as response:
            rates = await response.json()
            await message.answer(text=f'From: {rates["base_currency_name"]}\n'
                                      f'To: {list(rates["rates"].values())[0]["currency_name"]}\n'
                                      f'Rate: {list(rates["rates"].values())[0]["rate"]}')
            await state.finish()


@dp.message_handler(commands='transliteration')
async def transliteration_options(message: types.Message):
    """
    Get a keyboard with options what kind of transliteration is required
    """
    await message.reply("Choose transliteration option", reply_markup=transliteration)


@dp.callback_query_handler(text_endswith='transliteration')
async def transliteration_option(call: types.CallbackQuery):
    """
    This handler sets a state, that depends on user's previous choice of a button.
    Next handler will be chosen depends on settled state
    """
    if call.data.split('_')[0] == 'armenianeastern':
        await states.Transliteration.armenianeastern.set()
    elif call.data.split('_')[0] == 'armenianwestern':
        await states.Transliteration.armenianwestern.set()
    elif call.data.split('_')[0] == 'georgian':
        await states.Transliteration.georgian.set()
    else:
        await call.message.edit_text(text="Smth goes wrong")
    await call.message.edit_text(text="Enter a text")


@dp.message_handler(state=states.Transliteration.armenianeastern)
async def transliteration_armenian_eastern(message: types.Message, state: FSMContext):
    """
    This handler makes transliteration from latin to eastern armenian
    """
    text = await armenian_transliteration_eastern(message.text)
    await message.answer(text=text)
    await state.finish()


@dp.message_handler(state=states.Transliteration.armenianwestern)
async def transliteration_armenian_western(message: types.Message, state: FSMContext):
    """
    This handler makes transliteration from latin to western armenian
    """
    text = await armenian_transliteration_western(message.text)
    await message.answer(text=text)
    await state.finish()


@dp.message_handler(state=states.Transliteration.georgian)
async def transliterations_georgian(message: types.Message, state: FSMContext):
    """
    This handler makes transliteration from latin to georgian
    """
    text = await georgian_transliteration(message.text)
    await message.answer(text=text)
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)