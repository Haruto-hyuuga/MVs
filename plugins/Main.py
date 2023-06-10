import os
import asyncio
from bot import Bot
from pyrogram import filters, enums
from config import GUIDE_GRAPH
from H.txt import*
from pyrogram.types import (
    Message,
    CallbackQuery,
    InputMediaPhoto,
    InputMediaAnimation
)
from H.PIC import EXPic
    

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    bot = client 
    data = query.data
    update = query.message
    if data == "Start":
        await update.delete()
        URL_B = await UL_B("Discover Bot Features/ Usage", GUIDE_GRAPH)
        await update.reply_photo(
            photo=EXPic,
            caption=f"{JEXP}\n\n👉🏻 {GUIDE_GRAPH}",
            reply_markup=URL_B
        )
                
    elif data == "close":
        await update.delete()
        try:
            await update.reply_to_message.delete()
        except:
            pass
