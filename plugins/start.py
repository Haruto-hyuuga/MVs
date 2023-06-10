from bot import Bot
from pyrogram import filters
from pyrogram.types import Message
from config import LOG_U
from H.HF import subscribed
from H.txt import START_MSG
from H.ib import START_B


@Bot.on_message(filters.command('start') & filters.private & subscribed)
async def start_command(bot: Bot, message: Message):
    user = message.from_user
    uid = user.id
    ment = user.mention
     
    await bot.send_message(
        message.chat.id,
        text=START_MSG,
        reply_markup=START_B,
        protect_content=True
    )
