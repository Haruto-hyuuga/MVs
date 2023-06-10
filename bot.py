from aiohttp import web
from plugins import web_server

import pyromod.listen
from pyrogram import Client, filters
import sys
from datetime import datetime

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN


from typing import Union
from config import BOTUSERNAME as botusername

def cmd(comm: Union[list, str]):
  res = list()
  if isinstance(comm, str):
    res.extend([comm, f"{comm}@{botusername}"])
  if isinstance(comm, list):
    for com in comm:
      res.extend([com, f"{com}@{botusername}"])
  return filters.command(res, prefixes=["/", "?", "$", "!", "#", "@", ",", ".", "+", "~", "™", ";", ":", "-", "_"]) 

def parse_com(com, key):
  try:
    r = com.split(key,1)[1]
  except KeyError:
    return None
  r = (r.split(" ", 1)[1] if len(r.split()) >= 1 else None)
  return r

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="IBRbot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=50,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        
        self.LOGGER(__name__).info(f"Bot Running..! ✅")
        self.username = usr_bot_me.username
        #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, 8080).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
