from pyrogram import __version__
from bot import Bot
from config import PREMIUM_INFO, START_MSG, REQUEST_INFO, PREMIUM
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from plugins.start import START_B 
from database.database import is_user_premium


Back_Home_B = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("BACK", callback_data = "fsHOMEback")
        ]
    ] 
)
Back_Premium_B = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("BACK", callback_data = "premium"),
            InlineKeyboardButton("BUY NOW?", user_id = 6058427902)
        ]
    ] 
)
PREMIUM_B = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("BACK", callback_data = "fsHOMEback"),
            InlineKeyboardButton("PREMIUM BOT ⭐", callback_data = "premiumfeatures")
        ]
    ] 
)

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "fsHOMEback":
        await query.message.edit_text(
            text = START_MSG.format(query.from_user.mention),
            disable_web_page_preview = True,
            reply_markup = START_B
        )
    elif data == "premium":
        user_id = query.from_user.id
        ISUB = await is_user_premium(user_id)
        await query.message.edit_text(
            text = PREMIUM.format(ISUB),
            disable_web_page_preview = True,
            reply_markup = PREMIUM_B
        )
    elif data == "premiumfeatures":
        await query.message.edit_text(
            text = PREMIUM_INFO,
            disable_web_page_preview = True,
            reply_markup = Back_Premium_B
        )
    elif data == "aboutfsbot":
        await query.message.edit_text(
            text = REQUEST_INFO,
            disable_web_page_preview = True,
            reply_markup = B_B
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
