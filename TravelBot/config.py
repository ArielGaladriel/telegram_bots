import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
WEATHER_API = str(os.getenv("WEATHER_API"))
CURRENCY_API = str(os.getenv("CURRENCY_API"))

HEROKU_APP_NAME = str(os.getenv('HEROKU_APP_NAME'))
TOKEN = str(os.getenv("TOKEN"))
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{BOT_TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)