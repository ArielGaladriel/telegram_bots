import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
WEATHER_API = str(os.getenv("WEATHER_API"))
CURRENCY_API = str(os.getenv("CURRENCY_API"))