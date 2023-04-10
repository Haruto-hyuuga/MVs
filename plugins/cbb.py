from pyrogram import __version__
from bot import Bot
from config import PREMIUM_INFO, START_MSG, REQUEST_INFO
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from plugins.start import START_B 

B_B = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("BACK", callback_data = "fsHOMEback")
        ]
    ] 
)

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "premium":
        await query.message.edit_text(
            text = PREMIUM_INFO,
            disable_web_page_preview = True,
            reply_markup = B_B
        )
    elif data == "fsHOMEback":
        await query.message.edit_text(
            text = START_MSG.format(query.from_user.mention),
            disable_web_page_preview = True,
            reply_markup = START_B
        )
    elif data == "abotbotfs":
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
