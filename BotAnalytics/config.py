import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN2"))
ADMIN_API = str(os.getenv("ADMIN_API"))