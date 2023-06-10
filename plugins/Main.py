import os
import asyncio
from bot import Bot
from pyrogram import filters, enums
from H.txt import*
from pyrogram.types import (
    Message,
    CallbackQuery,
    InputMediaPhoto,
    InputMediaAnimation
)

    

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    bot = client 
    data = query.data
    update = query.message
    if data == "Start":
        await update.reply("hi")
                
    elif data == "close":
        await update.delete()
        try:
            await update.reply_to_message.delete()
        except:
            pass
