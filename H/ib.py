# ANIME ROBOTS                                                                                                                                                                                                                                                                                                                                                                                          
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import FORCE_SUB_URL, CONTACT_URL, OWNER_ID, GC_URL


S1_B = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("I'M JUST EXPLORING 🌐", callback_data="exploring")
        ],
        [
            InlineKeyboardButton("CREATE BOT FOR MY GROUP ⚡", callback_data="new_start")
        ]
    ]
)

async def CD_B(B_TEXT, B_DATA) -> InlineKeyboardMarkup:
    CD_B = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(f"{B_TEXT}", callback_data=f"{B_DATA}"),
        ],
    ])
    return CD_B

async def UL_B(B_TEXT, B_LINK) -> InlineKeyboardMarkup:
    URL_B = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(f"{B_TEXT}", url=f"{B_LINK}"),
        ],
    ])
    return URL_B


START_B = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("𝗔𝗖𝗖𝗢𝗨𝗡𝗧𝗦 🔏", callback_data="Accounts_cb"),
            InlineKeyboardButton("𝗦𝗘𝗧𝗧𝗜𝗡𝗚𝗦 ⚙️", callback_data="Settings_cb")
        ],
        [
            InlineKeyboardButton("📱𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦", callback_data="Commands"), 
            InlineKeyboardButton("𝗛𝗘𝗟𝗣 ⛑️", callback_data="Help_cb"),
        ],
        [
            InlineKeyboardButton("𝗔𝗕𝗢𝗨𝗧 ℹ️", callback_data="About_cb")
        ]
    ]
) 

FS_START_B = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🚀 JOIN AND GET STARTED 🚀", url=FORCE_SUB_URL)
        ]
    ]
)
