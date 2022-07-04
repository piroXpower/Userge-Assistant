# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge-Assistant > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Userge-Assistant/blob/master/LICENSE >
#
# All rights reserved.

import time
import random

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FileIdInvalid, FileReferenceEmpty, BadRequest

from assistant import bot, cus_filters, versions
from assistant.bot import START_TIME
from assistant.utils import time_formatter


file_id = [
]

@bot.on_message(filters.command("alive") & cus_filters.auth_chats)
async def _alive(_, message: Message, chat_id)
    caption = f"""
**🤖 Bot Uptime** : `{time_formatter(time.time() - START_TIME)}`
**🤖 Bot Version** : `{versions.__assistant_version__}`
**️️⭐ Python** : `{versions.__python_version__}`
**💥 Pyrogram** : `{versions.__pyro_version__}` """
    button = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="License",
                    url=("https://github.com/"
                         "Team/-Deadly/DEADLY-SPAMBOT/blob/master/LICENSE")),
                InlineKeyboardButton(
                    text="Repo",
                    url="https://github.com/Team-Deadly/DEADLY-SPAMBOT")
            ]
        ]
    )
    file_id = random.choice(LOGO_DATA)
    await bot.reply_photo(chat_id=chat_id,
                             photo=file_id,
                             caption=caption,
                             reply_markup=button)
