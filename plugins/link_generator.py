#(©)Codexbotz

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot
from config import ADMINS, CREATOR_GC
from helper_func import encode, get_message_id

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('batch'))
async def batch(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(text = "Forward the First Message from DB Channel (with Quotes)..\n\nor Send the DB Channel Post Link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue

    while True:
        try:
            second_message = await client.ask(text = "Forward the Last Message from DB Channel (with Quotes)..\nor Send the DB Channel Post link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        else:
            await second_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue


    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    await second_message.reply_text(f"<b>Here is your link</b>\n\n{link}", quote=True, reply_markup=reply_markup)


@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('genlink'))
async def link_generator(client: Client, message: Message):
    while True:
        try:
            channel_message = await client.ask(text = "Forward Message from the DB Channel (with Quotes)..\nor Send the DB Channel Post link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        else:
            await channel_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is not taken from DB Channel", quote = True)
            continue

    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    await channel_message.reply_text(f"<b>Here is your link</b>\n\n{link}", quote=True, reply_markup=reply_markup)

from database.database import present_pro_user, add_pro_user

@Bot.on_message(filters.command("addpro") & filters.user(ADMINS))
async def on_start(client: Bot, message: Message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        name = f"{message.reply_to_message.from_user.first_name} {message.reply_to_message.from_user.last_name}"
        uname = message.reply_to_message.from_user.username
        date = message.reply_to_message.date
        mention = message.reply_to_message.from_user.mention
        if not await present_pro_user(user_id):
            try:
                await add_pro_user(user_id, name, uname, date)
                await message.reply_text(f"ADDED USER {mention} AS PREMIUM\n\nUID: {user_id}\nFULL NAME: {name}\nUSERNAME: @{uname}\nDATE: {date}")
            except Exception as e:
                await message.reply_text(f"An Error Occured//-\n\n{e}")
        else:
            await message.reply_text(f"User: {mention} Alredy Premium")
    elif len(message.command) != 1 and not message.reply_to_message:
        text = message.text.split(None, 1)[1]
        user = await client.get_users(text)
        user_id = user.id
        name = f"{user.first_name} {user.last_name}"
        uname = user.username
        date = message.date
        mention = user.mention
        if not await present_pro_user(user_id):
            try:
                await add_pro_user(user_id, name, uname, date)
                await message.reply_text(f"ADDED USER {mention} AS PREMIUM\n\nUID: {user_id}\nFULL NAME: {name}\nUSERNAME: @{uname}\nDATE: {date}")
            except Exception as e:
                await message.reply_text(f"An Error Occured//-\n\n{e}")
        else:
            await message.reply_text(f"User: {mention} Alredy Premium")
    else:
        await message.reply_text(f"Bish Reply To User or Mention User After Command!")

