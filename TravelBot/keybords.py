from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

city_choice = InlineKeyboardMarkup(inline_keyboard=[
     [
         InlineKeyboardButton(text="Dilijan", callback_data='city_dilijan'),
         InlineKeyboardButton(text="Yerevan", callback_data='city_yerevan'),
         InlineKeyboardButton(text="Tbilisi", callback_data='city_tbilisi')
     ],
     [
         InlineKeyboardButton(text="Other", callback_data='other_weather')
     ],
     [
         InlineKeyboardButton(text="Back", callback_data="back")
     ]
 ])


currency_choise = InlineKeyboardMarkup(inline_keyboard=[
     [
         InlineKeyboardButton(text="RUB-AMD", callback_data='currency_rub_amd'),
         InlineKeyboardButton(text="USD-RUB", callback_data='currency_usd_rub'),
         InlineKeyboardButton(text="GEL-RUB", callback_data='currency_gel_rub')
     ],
     [
         InlineKeyboardButton(text="USD-AMD", callback_data='currency_usd_amd'),
         InlineKeyboardButton(text="USD-GEL", callback_data='currency_usd_gel'),
         InlineKeyboardButton(text="GEL-AMD", callback_data='currency_gel_amd')
     ],
     [
         InlineKeyboardButton(text="Other", callback_data='other_currency')
     ],
     [
         InlineKeyboardButton(text="Back", callback_data="back")
     ]
 ])