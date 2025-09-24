
from os import getenv

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "8075836012"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "")
LOG_GROUP = int(getenv("LOG_GROUP", "-1003082043736"))
FORCESUB = getenv("FORCESUB", "-1003025510345")
DEFAULT_SESSION = getenv("DEFAULT_SESSION", "") # this is just to help if you dont want to force your bot user to login or if they not interested

