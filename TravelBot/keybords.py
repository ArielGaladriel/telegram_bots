from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

city_choice = InlineKeyboardMarkup(inline_keyboard=[
     [
         InlineKeyboardButton(text="Dilijan", callback_data='city_dilijan'),
         InlineKeyboardButton(text="Yerevan", callback_data='city_yerevan'),
         InlineKeyboardButton(text="Tbilisi", callback_data='city_tbilisi')
     ],
     [
         InlineKeyboardButton(text="Other", callback_data='other')
     ],
     [
         InlineKeyboardButton(text="Back", callback_data="back")
     ]
 ])