from aiogram.dispatcher.filters.state import StatesGroup, State


class City(StatesGroup):
    city = State()


class Country(StatesGroup):
    country = State()