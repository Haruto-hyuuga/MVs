from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot
from database.database import present_pro_user
from config import FORCE_SUB_CHANNEL, CHANNEL_URL

PRO_WRONG_FORWARD = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("EXPLORE MORE CONTENT", url = CHANNEL_URL)
        ]
    ]
)

NO_PRO_B_F = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("PREMIUM STATUS", callback_data = "premium"),
            InlineKeyboardButton("PREMIUM FETURES", callback_data = "premiumfeatures")
        ]
    ]
)

@Bot.on_message(filters.private & filters.forwarded)
async def batch(client: Client, message: Message):
    user_id = message.from_user.id
    if message.forward_from_chat.id == FORCE_SUB_CHANNEL:
        if await present_pro_user(user_id):
            await message.reply_text("NOT MADE YET XD")
        else:
            await message.reply_text("You're Not Premium User Retard", reply_markup=NO_PRO_B_F)
    else:
        await message.reply_text("PLEASE FORWARD POST FROM CHANNEL WITH QUOTE (don't change sender's name)", reply_markup=PRO_WRONG_FORWARD)
        
