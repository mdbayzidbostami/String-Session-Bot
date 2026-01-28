import os
from typing import List

API_ID = os.environ.get("API_ID", "22005506")
API_HASH = os.environ.get("API_HASH", "af9406c860b34bd575b04f2b555bb6b0")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8377038535:AAF8P00IYaqXibyrkKLSe6jcWPgizVlAQbc")
ADMIN = int(os.environ.get("ADMIN", "5548923721"))
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002549272838"))
DB_URI = os.environ.get("DB_URI", "mongodb+srv://xeroxbayzid12:xeroxbayzid12@cluster0.dcapc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "xeroxbayzid12")
IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1002549272838").split())) # Add Multiple channel ids
AUTH_REQ_CHANNELS = list(map(int, os.environ.get("AUTH_REQ_CHANNEL", "-1002549272838").split())) # Add Multiple channel ids
FSUB_EXPIRE = int(os.environ.get("FSUB_EXPIRE", 2))  # minutes, 0 = no expiry
