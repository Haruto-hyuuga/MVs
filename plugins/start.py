import os
import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated

from bot import Bot
from config import ADMINS, FORCE_MSG, START_MSG, PROTECT_CONTENT, CHANNEL_URL, PREMIUM, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON
from helper_func import subscribed, encode, decode, get_messages
from database.database import add_user, del_user, full_userbase, present_user, del_pro_user, present_pro_user

START_B = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("⭐ PREMIMUM", callback_data = "premium"),
            InlineKeyboardButton("ℹ️ ABOUT", callback_data = "aboutfsbot")
        ],
        [
            InlineKeyboardButton("EXPLORE MORE CONTENT", url = CHANNEL_URL)
        ]
    ]
)
PRO_WRONG_FORWARD = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("EXPLORE MORE CONTENT", url = CHANNEL_URL)
        ]
    ]
)
POST_B = InlineKeyboardMarkup(
    [
        [
       #     InlineKeyboardButton("⭐ PREMIMUM", callback_data = "premium"),
            InlineKeyboardButton("MORE VIDEOS ♥️", url = CHANNEL_URL)
        ]
    ]
)


@Bot.on_message(filters.command('start') & filters.private & subscribed)
async def start_command(client: Client, message: Message):
    id = message.from_user.id
    if not await present_user(id):
        try:
            await add_user(id)
        except:
            pass
    text = message.text
    if len(text)>7:
        try:
            base64_string = text.split(" ", 1)[1]
        except:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except:
                return
            if start <= end:
                ids = range(start,end+1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except:
                return
        try:
            messages = await get_messages(client, ids)
        except:
            await message.reply_text("Something went wrong..!")
            return
        for msg in messages:
            
            if bool(CUSTOM_CAPTION) & bool(msg.document):
                caption = CUSTOM_CAPTION.format(previouscaption = "" if not msg.caption else msg.caption.html, filename = msg.document.file_name)
            else:
                caption = "" if not msg.caption else msg.caption.html

            if DISABLE_CHANNEL_BUTTON:
                reply_markup = msg.reply_markup
            else:
                reply_markup = None

            try:
                await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = ParseMode.HTML, reply_markup = POST_B, protect_content=PROTECT_CONTENT)
                await asyncio.sleep(0.5)
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = ParseMode.HTML, reply_markup = POST_B, protect_content=PROTECT_CONTENT)
            except:
                pass
        return
    else:
        await message.reply_text(
            text = START_MSG.format(message.from_user.mention),
            reply_markup = START_B,
            disable_web_page_preview = True,
            quote = True
        )
        return

    
#=====================================================================================##

WAIT_MSG = """"⏳"""

REPLY_ERROR = """<code>Use this command as a replay to any telegram message with out any spaces.</code>"""

#=====================================================================================##

    
    
@Bot.on_message(filters.command('start') & filters.private)
async def not_joined(client: Client, message: Message):
    buttons = [
        [
            InlineKeyboardButton(
                "Join Channel",
                url = client.invitelink)
        ]
    ]
    try:
        buttons.append(
            [
                InlineKeyboardButton(
                    text = 'Try Again',
                    url = f"https://t.me/{client.username}?start={message.command[1]}"
                )
            ]
        )
    except IndexError:
        pass

    await message.reply(
        text = FORCE_MSG,
        reply_markup = InlineKeyboardMarkup(buttons),
        quote = True,
        disable_web_page_preview = True
    )


from datetime import datetime
from helper_func import get_readable_time

@Bot.on_message(filters.command(['stats', 'ping']) & filters.private & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    users = await full_userbase()
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    await msg.edit(f"UPTIME: {time} \nUSERS: {len(users)}")

@Bot.on_message(filters.command('broadcast') & filters.user(ADMINS))
async def send_text(client: Bot, message: Message):
    if message.reply_to_message:
        query = await full_userbase()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0
        
        pls_wait = await message.reply(WAIT_MSG)
        for chat_id in query:
            try:
                await broadcast_msg.copy(chat_id)
                successful += 1
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await broadcast_msg.copy(chat_id)
                successful += 1
            except UserIsBlocked:
                await del_user(chat_id)
                blocked += 1
            except InputUserDeactivated:
                await del_user(chat_id)
                deleted += 1
            except:
                unsuccessful += 1
                pass
            total += 1
        
        status = f"""<b><u>Broadcast Completed</u>

Total Users: <code>{total}</code>
Successful: <code>{successful}</code>
Blocked Users: <code>{blocked}</code>
Deleted Accounts: <code>{deleted}</code>
Unsuccessful: <code>{unsuccessful}</code></b>"""
        
        return await pls_wait.edit(status)

    else:
        msg = await message.reply(REPLY_ERROR)
        await asyncio.sleep(8)
        await msg.delete()



@Bot.on_message(filters.command("delpro") & filters.user(ADMINS))
async def on_start(client: Bot, message: Message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        mention = message.reply_to_message.from_user.mention
        if await present_pro_user(user_id):
            try:
                await del_pro_user(user_id)
                await message.reply_text(f"REMOVED USER {mention} FROM PREMIUM\n\nUID: {user_id}")
            except Exception as e:
                await message.reply_text(f"An Error Occured//-\n\n{e}")
        else:
            await message.reply_text(f"User: {mention} NEVER WAS PREMIUM")
    elif len(message.command) != 1 and not message.reply_to_message:
        text = message.text.split(None, 1)[1]
        user = await client.get_users(text)
        user_id = user.id
        mention = user.mention
        if await present_pro_user(user_id):
            try:
                await del_pro_user(user_id)
                await message.reply_text(f"REMOVED USER {mention} FROM PREMIUM\n\nUID: {user_id}")
            except Exception as e:
                await message.reply_text(f"An Error Occured//-\n\n{e}")
        else:
            await message.reply_text(f"User: {mention} NEVER WAS PREMIUM")
    else:
        await message.reply_text(f"Bish Reply To User or Mention User After Command!")
