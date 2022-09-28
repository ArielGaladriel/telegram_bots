from aiogram.dispatcher.filters.state import StatesGroup, State


class City(StatesGroup):
    city = State()


class Country(StatesGroup):
    country = State()


class Transliteration(StatesGroup):
    armenianeastern = State()
    armenianwestern = State()
    georgian = State()
