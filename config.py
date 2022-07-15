import os
from pyrogram import *
from pyrogram.types import *

API_ID = os.getenv("API_ID", "").strip()
API_HASH = os.getenv("API_HASH", "").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
MONGO_URI = os.getenv("MONGO_URI", "").strip()
AUTH_CHANNEL = os.getenv("AUTH_CHANNEL", "").strip()
BOT_USERNAME = os.getenv("BOT_USERNAME", "").strip()
AUTH_USERS = os.getenv("AUTH_USERS", "").strip()
LOG_CHANEL = os.getenv("LOG_CHANEL", "").strip()
