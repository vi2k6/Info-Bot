# Made with Python3
# (C) FayasNoushad and Vivek-TP

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Bot = Client(
        "Info Bot",
        bot_token = os.environ["BOT_TOKEN"],
        api_id = int(os.environ["API_ID"]),
        api_hash = os.environ["API_HASH"]
)

START_TEXT = """
<b>Hello {}

I am a Simple Telegram Info Gathering Bot, Click /help to know my Commands and my uses<b>
"""
HELP_TEXT = """
🤔 How to use me?

⭕️ Forward a Message for take it's Details (in Private)

⭕️ Send any Media to take its Details (in private)

⭕️ Reply /info to a Message to take Message Details

⭕️ Use /info Command to take your Details

⭕️ Use /id in Group or Channel to get Unique Telegram ID
"""
ABOUT_TEXT = """
**Bot :** `Info Bot`
**Creator :** [Vivek](https://telegram.me/Vivek_KERALA)
**Credits :** `Everyone in this journey`
**Source :** [Click here](https://github.com/vivek-tp/Info-Bot)
**Language :** [Python3](https://python.org)
**Library :** [Pyrogram v1.2.0](https://pyrogram.org)
**Server :** [Heroku](https://heroku.com)
"""

Bot = Client(
        "Maintenance Bot",
        bot_token = os.environ["BOT_TOKEN"],
        api_id = int(os.environ["API_ID"]),
        api_hash = os.environ["API_HASH"]
)

supportc = os.environ["SUPPORT_CHAT"]

BOT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Support", url=f"https://telegram.me/{supportc}")
        ]]
    )


START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Support", url=f"https://telegram.me/{supportc}")
        ]]
    )

HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Support", url=f"https://telegram.me/{supportc}")
        ]]
    )

ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Support", url=f"https://telegram.me/{supportc}")
        ]]
    )
                
@Bot.on_message(filters.private & filters.command("start"))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention) 
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@Bot.on_message(filters.private & filters.command("help"))
async def help(bot, update):
    text = HELP_TEXT
    reply_markup = HELP_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )


@Bot.on_message(filters.private & filters.command("about"))
async def about(bot, update):
    text = ABOUT_TEXT
    reply_markup = ABOUT_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@Bot.on_message(filters.private & filters.command("info"))
async def info(bot, update):
    # Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)
    # (C) FayasNoushad # All rights reserved # Made with Python3
    info = f"**{update.from_user.first_name}'s Informations**\n"
    info += f"\n**First Name :** {update.from_user.first_name}"
    if update.from_user.second_name:
        info += f"\n**Second Name :** {update.from_user.second_name}"
    if update.from_user.username:
        info += f"\n**Username :** {update.from_user.username}"
    info += f"\n**ID :** {update.from_user.id}"
    info += f"\n**Status :** {update.from_user.status}"
    info += f"\n**Data Center :** {update.from_user.dc_id}"
    info += f"\n**Type :** {update.from_user._}"
    reply_markup = BOT_BUTTONS
    await update.reply_text(        
        text=info,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@Bot.on_message(filters.private & filters.command("id"))
async def id(bot, update):
    text = f"""
**Your Telegram ID :** {update.from_user.id}
"""
    reply_markup = BOT_BUTTONS
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

Bot.run()
