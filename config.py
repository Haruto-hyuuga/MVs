import os
import logging
from logging.handlers import RotatingFileHandler


TG_BOT_TOKEN = ""
APP_ID = 12585681
API_HASH = "7741e8a55a0b5174548c52a374ab94b8"
# main channel
FORCE_SUB_CHANNEL = 
CHANNEL_URL = "https://t.me/"
DB_URI = ""

# database channel
CHANNEL_ID = 
CREATOR_GC = -1001977466101
PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

pro_channel_url = "https://t.me/adultsegsvideos"
pro_bot_url = "https://t.me/HORNYSOCIETY18"

START_MSG = """Welcome {}
Trough This Bot You Can Download Movies From Our Channel For Free!
Search Movies on: 
"""

FORCE_MSG = """
ONLY MEMBERS OF MY CHANNEL CAN USE THIS BOT.
JOIN: @HORNYSOCIETY18
AND TRY AGAIN ♥️
"""

PREMIUM = """
Check Out Some Of Our Hot Channels
"""

REQUEST_INFO = """
> Made and Hosted By: @AnimeRobots 🌐
> ONLINE SINCE: 10 April, 2023
> Don't delete the bot or all the files you have in bot will be deleted.
"""

ADMINS = []
if not 1497264683 in ADMINS:  #Shiro
  ADMINS.append(1497264683)
if not 6058427902 in ADMINS:  # bot owner 
  ADMINS.append(6058427902)


CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
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
