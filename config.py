# Rexa Bau

from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")

SUDO_USER = list(
    map(int, getenv("SUDO_USER", "").split())
)  # Input type must be interger


MONGO_DB_URI = getenv("MONGO_DB_URI", None)
