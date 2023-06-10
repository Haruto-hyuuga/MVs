APP_ID = 19879178
API_HASH = "b3d8705ed82a2f4ba5f4520d8d9b51a6"
TG_BOT_TOKEN = "6118754543:AAGicz-5pZUif7Ymg5LlBhsRIe2i3uHAduM"
BOTUSERNAME = "GroupMaid1_Robot"

LOG_E = -1001879984748
LOG_U = -1001879984748
LOG_P = -1001879984748
 


GUIDE_GRAPH = "https://graph.org/Maid-ROBOT-EXPO-06-10"
GC_URL = "https://t.me/AnimeCommunityChat"
FORCE_SUB_CHANNEL = -1001867076149
FORCE_SUB_URL = "https://t.me/AnimeRobots/30"

OWNER_ID = 1497264683
CONTACT_URL = "http://t.me/Maid_Robot"
DEV = []
if not 1497264683 in DEV:  # Shiro
  DEV.append(1497264683)
if not 5024928504 in DEV:  # mei
  DEV.append(5024928504)
if not 1302714537 in DEV:  # DSp
  DEV.append(1302714537)
if not 5296520170 in DEV:  # emi
  DEV.append(5296520170)
if not 5329765587 in DEV:  # schwi
  DEV.append(5329765587)

  
USER_DB = ""
ACCOUNT_DB = ""
  
  
  
  
  
  
  
  
  
  
  

import logging
from logging.handlers import RotatingFileHandler
LOG_FILE_NAME = "bgirmebot.txt"

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
