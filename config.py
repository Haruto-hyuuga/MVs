import os
import logging
from logging.handlers import RotatingFileHandler


TG_BOT_TOKEN = "6280133291:AAHyAMxzRIzCjz2Cj2a-_WklR2GThyRz3HI"
APP_ID = 12585681
API_HASH = "7741e8a55a0b5174548c52a374ab94b8"
CHANNEL_ID = -1001923785404
OWNER_ID = 1497264683
FORCE_SUB_CHANNEL = -1001980726161
DB_URI = "mongodb+srv://hasab93439:oq34A8uJvf07gPpS@cluster0.etxxg29.mongodb.net/?retryWrites=true&w=majority"
CREATOR_GC = -1001977466101

PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))


START_MSG = "Hello {}\n\nI can store private files in Specified Channel and other users can access it from special link."
FORCE_MSG = "Hello {}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>"
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "HM CAPTION")
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False
PREMIUM_INFO = """
OK
"""
REQUEST_INFO = """
hm
"""
CHANNEL_URL = ""

TG_BOT_TOKEN2 = "5517964484:AAGHsv77whs_v1r50AUHBz4OEIgMfQxa5FU"
APP_ID2 = 27178732
API_HASH2 = "daa4f389a237076b5f6b46f25ea4c865"

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")




#set True if you want to prevent users from forwarding files from bot


#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
