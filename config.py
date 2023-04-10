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


START_MSG = """Welcome {}
Trough This Bot You Can Access P🔞RN Content From Our Channel.
Now Go To Channel- @secretsociety_18 and start bot from link given in post.
"""

FORCE_MSG = """
ONLY MEMBERS OF MY CHANNEL CAN USE THIS BOT.
JOIN: @secretsociety_18
AND TRY AGAIN ♥️
"""


PREMIUM_INFO = """
BOT⭐ @secretsociety_PRObot

PREMIUM BOT FEATURES:
✰ You'll be able to access content of our channel Directly Without any Redirect Link.
✰ You'll be able to save and forward media.
✰ Allow Requests: You can send Links From Browser containing Media And Bot will Download and make it available for you.
✰ Unlock Illegal Stuff.
"""
REQUEST_INFO = """
> Made and Hosted By: @AnimeRobots 🌐
> ONLINE SINCE: 10 April, 2023
> Don't delete the bot or all the files you have in bot will be deleted.
"""

CHANNEL_URL = "http://t.me/secretsociety_18"


ADMINS = []
if not 1497264683 in ADMINS:  #Shiro
  ADMINS.append(1497264683)
if not 6058427902 in ADMINS:  # bot owner 
  ADMINS.append(6058427902)


CUSTOM_CAPTION = "Checkout: @fsecxbot 🔞"
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
