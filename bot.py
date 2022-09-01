import os
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


Bot = Client(
    "Info Bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)

START_TEXT = """<b>Hello {}

I am a Simple Telegram Info Gathering Bot, Click /help to know my Commands and my uses<b>"""

HELP_TEXT = """🤔 How to use me?

• Forward a Message for take it's Details (in Private)
• Send any Media to take its Details (in private)
• Reply /info to a Message to take Message Details
• Use /chatinfo In Any Chats to get info about chat
• Use /info Command to take your Details
• Use /id in Group or Channel to get Unique Telegram ID"""

ABOUT_TEXT = """--**About Me**--

- **Bot :** [FIND ID Bot](https://t.me/Find_IDBot)
- **Creator :** [Vɪᴠᴇᴋ](https://telegram.me/Vivek2k6)
- **Language :** [Python3](https://python.org)
- **Library :** [Pyrogram v1.2.0](https://pyrogram.org)
- **Server :** [Heroku](https://heroku.com)
- **Channel :** [My Own Bots](https://t.me/myownbots)
- **Support :** [Bot Support](https://t.me/devschats)"""

START_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Channel', url='https://telegram.me/MyOwnBots'),
            InlineKeyboardButton('Support', url='https://telegram.me/DevsChats')
        ],
        [
            InlineKeyboardButton('Help', callback_data='help'),
            InlineKeyboardButton('About', callback_data='about')
        ]
    ]
)

HELP_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Home', callback_data='home'),
            InlineKeyboardButton('About', callback_data='about')
        ]
    ]
)

ABOUT_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Home', callback_data='home'),
            InlineKeyboardButton('Help', callback_data='help')
        ]
    ]
)

@Bot.on_callback_query()
async def cb_data(bot, update):
    
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTON
        )
    
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTON
        )
    
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTON
        )
    
    else:
        await update.message.delete()

@Bot.on_message(filters.private & filters.command("start"))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTON
    )


@Bot.on_message(filters.private & filters.command("help"))
async def help(bot, update):
    await update.reply_text(
        text=HELP_TEXT,
        disable_web_page_preview=True,
        reply_markup=HELP_BUTTON
    )


@Bot.on_message(filters.private & filters.command("about"))
async def about(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT,
        disable_web_page_preview=True,
        replay_markup=ABOUT_BUTTON
    )


@Bot.on_message(filters.private & filters.command("info"))
async def info(bot, update):
    
    text = f"""--**Information**--

**First Name :** {update.from_user.first_name}
**Second Name :** {update.from_user.last_name if update.from_user.last_name else 'None'}
**DC :** {update.from_user.dc_id}
**Username :** {update.from_user.username}
**Telegram ID :** {update.from_user.id}
**Profile Link :** {update.from_user.mention}"""
    
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True
    )


@Bot.on_message(filters.private & filters.command("id"))
async def id(bot, update):
    await update.reply_text(        
        text=f"**Your Telegram ID :** {update.from_user.id}",
        disable_web_page_preview=True
    )

@Bot.on_message(filters.group & filters.command("id"))
async def id(bot, update):
    await update.reply_text(        
        text=f"**Telegram ID :** {update.chat.id}
**DC :** {update.chat.dc_id}
**Name :** {update.chat.title}
**Type :** {update.chat.type}
**Members :** {update.chat.members_count}
**Username :** {update.chat.username}
**Is Scam? :** {update.chat.is_scam}
**Description :** {update.chat.discription}
**Restricted :** {update.chat.is_restricted}",
        disable_web_page_preview=True
    )


print("Bot Started!!! Now Join on @MyOwnBots")
Bot.run()
