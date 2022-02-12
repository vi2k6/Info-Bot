import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


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
• Use /info Command to take your Details
• Use /id in Group or Channel to get Unique Telegram ID"""

ABOUT_TEXT = """--**About Me**--

- **Bot :** `Info Bot`
- **Creator :** [Vivek](https://telegram.me/Vivek_KERALA)
- **Credits :** `Everyone in this journey`
- **Source :** [Click here](https://github.com/vivek-tp/Info-Bot)
- **Language :** [Python3](https://python.org)
- **Library :** [Pyrogram v1.2.0](https://pyrogram.org)
- **Server :** [Heroku](https://heroku.com)"""

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton(text="SOURCE", url=f"https://github.com/vivek-tp/Info-Bot")]])


@Bot.on_message(filters.private & filters.command("start"))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=BUTTONS
    )


@Bot.on_message(filters.private & filters.command("help"))
async def help(bot, update):
    await update.reply_text(
        text=HELP_TEXT,
        disable_web_page_preview=True,
        reply_markup=BUTTONS
    )


@Bot.on_message(filters.private & filters.command("about"))
async def about(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT,
        disable_web_page_preview=True,
        reply_markup=BUTTONS
    )


@Bot.on_message(filters.private & filters.command("info"))
async def info(bot, update):
    
    text = f"""--**Information**--

**🙋🏻‍♂️ First Name :** {update.from_user.first_name}
**🧖‍♂️ Your Second Name :** {update.from_user.last_name if update.from_user.last_name else 'None'}
**🧑🏻‍🎓 Your Username :** {update.from_user.username}
**🆔 Your Telegram ID :** {update.from_user.id}
**🔗 Your Profile Link :** {update.from_user.mention}"""
    
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=BUTTONS
    )


@Bot.on_message(filters.private & filters.command("id"))
async def id(bot, update):
    await update.reply_text(        
        text=f"**Your Telegram ID :** {update.from_user.id}",
        disable_web_page_preview=True,
        reply_markup=BUTTONS
    )


print("Bot Started!!! Now Join on @Vkprojects")
Bot.run()
