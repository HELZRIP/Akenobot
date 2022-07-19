import asyncio
import telegram
import os
import requests
import datetime
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom, version
from AsukaRobot.events import register
from AsukaRobot import telethn as borg, OWNER_ID, OWNER_NAME
from AsukaRobot import StartTime, dispatcher
from telethon.tl.types import ChannelParticipantsAdmins
from pyrogram import __version__ as pyro


edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://te.legra.ph/file/ce84881970d9514a62fd4.jpg"
file2 = "https://te.legra.ph/file/5e16d1ce34d58bca8bdde.jpg"
file3 = "https://te.legra.ph/file/4ea17f15d61bd7df808be.jpg"
file4 = "https://te.legra.ph/file/ce057de710c7a05ae14c4.jpg"
""" =======================CONSTANTS====================== """

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

@register(pattern=("/alive"))
async def hmm(yes):
    chat = await yes.get_chat()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    Asuka = f"• **Hey [{yes.sender.first_name}](tg://user?id={yes.sender.id}), I'm 𝒜𝓀ℯ𝓃ℴ**\n"
    Asuka += f"• **My Uptime** - `{uptime}`\n"
    Asuka += f"• **Telethon Version** - `{version.__version__}`\n"
    Asuka += f"• **PTB Version** - `{telegram.__version__}`\n"
    Asuka += f"• **Pyrogram Version** - `{pyro}`\n"
    Asuka += f"• **My Master** - [Dream Garden](tg://user?id={OWNER_ID})\n\n"
    Asuka += f"Thanks For Adding Me In {yes.chat.title}"
    BUTTON = [[Button.url("Support Chat", "https://t.me/Rsupportprobot"), Button.url("Updates", "https://t.me/Akeno_update")]]
    on = await borg.send_file(yes.chat_id, file="https://te.legra.ph/file/ce84881970d9514a62fd4.jpg",caption=Asuka, buttons=BUTTON)

@register(pattern=("/repo"))
async def repo(yes):
    Asuka = f"**Hey [{event.sender.first_name}](tg://user?id={event.sender.id}), Click The Button Below To Get My Repo**\n\n"
    BUTTON = [[Button.url("GitHub", "https://t.me/helzrip"), Button.url("Developer", "https://t.me/helzrip")]]
    await borg.send_file(event.chat_id, file="https://te.legra.ph/file/ce84881970d9514a62fd4.jpg", caption=Akeno, buttons=BUTTON)
