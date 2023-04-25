from pyrogram import __version__
from bot import Bot
from config import pro_bot_url, START_MSG, REQUEST_INFO, PREMIUM, pro_channel_url
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from plugins.start import START_B 


Back_Home_B = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("BACK", callback_data = "fsHOMEback")
        ]
    ] 
)

PREMIUM_B = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("♥️ PREMIUM CHANNEL ♥️", url=pro_channel_url)
        ],
        [
            InlineKeyboardButton("⭐ PREMIUM BOT ⭐", url=pro_bot_url)
        ],
        [
            InlineKeyboardButton("BACK", callback_data = "premium"),
            InlineKeyboardButton("BUY NOW?", user_id = 6058427902)
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
        await query.message.edit_text(
            text = PREMIUM,
            disable_web_page_preview = True,
            reply_markup = PREMIUM_B
        )
    elif data == "aboutfsbot":
        await query.message.edit_text(
            text = REQUEST_INFO,
            disable_web_page_preview = True,
            reply_markup = Back_Home_B
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
