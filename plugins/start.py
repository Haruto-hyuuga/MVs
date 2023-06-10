from bot import Bot, cmd
from pyrogram import filters
from pyrogram.types import Message
from config import LOG_U
from H.HF import subscribed
from H.txt import S1_MSG
from H.ib import S1_B


@Bot.on_message(cmd(['start']) & filters.private & subscribed)
async def start_command(bot: Bot, message: Message):
    user = message.from_user
    uid = user.id
    ment = user.mention
     
    await bot.send_message(
        message.chat.id,
        text=S1_MSG,
        reply_markup=S1_B,
        protect_content=True
    )
